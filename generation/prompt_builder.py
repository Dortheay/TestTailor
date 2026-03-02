"""
Prompt Builder
==============
Assembles all components collected in stages 1 and 2 into the final LLM
prompt, following the template in Figure 6 of the paper:

    ┌─────────────────────────────────────────┐
    │ Function under Test                     │  ← Contextual Preprocessing
    │ Relevant Information from project       │
    │ The Target code unit                    │
    │─────────────────────────────────────────│
    │ Symbolic constraints                    │  ← Fine-Grained Path Analysis
    │ Most Path-Proximal test case            │
    │ Path Divergence Analysis                │
    │─────────────────────────────────────────│
    │ Your task / formatting instructions     │  ← Generation instructions
    └─────────────────────────────────────────┘

Two prompt types are produced:
  - initial_prompt   : first generation attempt
  - repair_prompt    : appended when the test has compilation/runtime errors
  - refine_prompt    : appended when the test runs but misses the target
"""

from typing import Optional

from models import (
    CodeUnit, DependencyContext, PathProximalTest, TargetPath
)
from path_analysis.symbolic_executor import format_constraints
from path_analysis.path_divergence import format_divergence


# ──────────────────────────────────────────────────────────────────────────────
# Section formatters
# ──────────────────────────────────────────────────────────────────────────────

def _section(title: str, body: str) -> str:
    bar = "=" * 60
    return f"{bar}\n{title}\n{bar}\n{body.strip()}\n"


def _format_deps(ctx: DependencyContext) -> str:
    parts = []
    if ctx.class_definition_src:
        parts.append(f"# Class definition\n{ctx.class_definition_src}")
    for dep in ctx.dependency_srcs:
        parts.append(dep)
    return "\n\n".join(parts) if parts else "(no additional dependencies)"


def _format_imports(ctx: DependencyContext) -> str:
    return "\n".join(ctx.imports) if ctx.imports else ""


# ──────────────────────────────────────────────────────────────────────────────
# Initial prompt
# ──────────────────────────────────────────────────────────────────────────────

INITIAL_PROMPT_TEMPLATE = """\
You are an expert Python test developer. Your task is to write a unittest test case
that covers a specific, currently uncovered code branch.

{imports}

{section_function}

{section_deps}

{section_target}

{section_constraints}

{section_proximal}

{section_divergence}

{section_task}
"""

TASK_INSTRUCTIONS = """\
Create a test case that targets the branch containing the target code unit shown above.
Use the reference test case as guidance and adapt it so that:
  1. The path conditions listed above are satisfied.
  2. The divergence point is resolved in favour of the target path.

Requirements:
  - Use unittest.TestCase style with a @timeout_decorator.timeout(1) decorator.
  - The test must be self-contained (no external state pollution).
  - Include at least one assertion that verifies a post-condition.
  - Do NOT include module-level calls to pytest.main or the test itself.
  - Only provide the completed test class starting from "class Test" line.
  - Do not include import statements (they are handled separately).

```python
# necessary import statements
class Test(unittest.TestCase):
    @timeout_decorator.timeout(1)
    def test_case(self):
        \"\"\"Complete the test case here\"\"\"
        ...
```

Respond ONLY with the Python code enclosed in backticks, without any explanation.
"""


def build_initial_prompt(
    ctx: DependencyContext,
    target_path: TargetPath,
    proximal: Optional[PathProximalTest],
) -> str:
    """
    Build the initial generation prompt (Figure 6).
    """
    unit = ctx.target_unit

    section_function = _section(
        "Function under Test",
        ctx.enclosing_function_src,
    )

    section_deps = _section(
        "Relevant Information from the Entire Project",
        _format_deps(ctx),
    )

    section_target = _section(
        "The Target Code Unit You Need to Cover",
        unit.code_snippet,
    )

    constraints_text = format_constraints(target_path)
    section_constraints = _section(
        "Path Constraints (conditions that must be satisfied to reach the target)",
        constraints_text,
    )

    if proximal:
        section_proximal = _section(
            "The Most Path-Proximal Test Case (use this as your reference)",
            proximal.test_source,
        )
        section_divergence = _section(
            "Path Divergence Analysis",
            format_divergence(proximal),
        )
    else:
        section_proximal = _section(
            "Path-Proximal Test Case",
            "(no existing test is close to the target path; generate from scratch)",
        )
        section_divergence = ""

    section_task = _section("Your Task", TASK_INSTRUCTIONS)

    imports = _format_imports(ctx)
    imports_block = f"# Relevant imports\n{imports}" if imports else ""

    prompt = INITIAL_PROMPT_TEMPLATE.format(
        imports=imports_block,
        section_function=section_function,
        section_deps=section_deps,
        section_target=section_target,
        section_constraints=section_constraints,
        section_proximal=section_proximal,
        section_divergence=section_divergence,
        section_task=section_task,
    )
    return prompt.strip()


# ──────────────────────────────────────────────────────────────────────────────
# Repair prompt (compilation / runtime errors)
# ──────────────────────────────────────────────────────────────────────────────

def build_repair_prompt(
    previous_prompt: str,
    previous_test: str,
    error_message: str,
) -> str:
    """
    Appended to the conversation when the generated test has errors.
    """
    return (
        f"{previous_prompt}\n\n"
        f"{'=' * 60}\n"
        f"Previous Attempt (FAILED)\n"
        f"{'=' * 60}\n"
        f"```python\n{previous_test}\n```\n\n"
        f"Error encountered:\n```\n{error_message}\n```\n\n"
        f"Please fix the test so that it compiles and runs without errors, "
        f"while still covering the target code unit.\n"
        f"Respond ONLY with the corrected Python code in backticks."
    )


# ──────────────────────────────────────────────────────────────────────────────
# Refine prompt (runs but misses coverage target)
# ──────────────────────────────────────────────────────────────────────────────

def build_refine_prompt(
    previous_prompt: str,
    previous_test: str,
    new_proximal: PathProximalTest,
    target_path: TargetPath,
) -> str:
    """
    Appended when the test executes correctly but does NOT cover the target unit.
    The previously generated test is now the new 'path-proximal' seed.
    """
    new_div = format_divergence(new_proximal)
    return (
        f"{previous_prompt}\n\n"
        f"{'=' * 60}\n"
        f"Previous Attempt (executed but did not cover the target)\n"
        f"{'=' * 60}\n"
        f"```python\n{previous_test}\n```\n\n"
        f"The test ran successfully but missed the target code unit.\n"
        f"Updated Path Divergence Analysis based on this new attempt:\n"
        f"{new_div}\n\n"
        f"Please adjust the test inputs / setup to resolve this remaining divergence.\n"
        f"Respond ONLY with the corrected Python code in backticks."
    )
