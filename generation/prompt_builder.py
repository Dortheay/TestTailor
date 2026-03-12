"""
Prompt Builder
==============
Assembles all components collected in stages 1 and 2 into the final LLM
prompt, following the template in the paper (Figure 6):

    ┌─────────────────────────────────────────┐
    │ Function under Test                     │  ← Contextual Preprocessing
    │ Relevant Information from the project   │
    │ The Target code unit you need to cover  │
    │─────────────────────────────────────────│
    │ To reach the target code, the test      │  ← Fine-Grained Path Analysis
    │   needs to satisfy conditions: <...>    │
    │ The most Path-Similar test case         │
    │ Path Divergence Analysis                │
    │─────────────────────────────────────────│
    │ Your task / formatting instructions     │  ← Explicit Formatting Instructions
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

def _heading(title: str, body: str) -> str:
    """Bold-style section heading followed by content (no heavy === bars)."""
    return f"**{title}**\n{body.strip()}"


def _format_deps(ctx: DependencyContext) -> str:
    parts = []
    if ctx.class_definition_src:
        parts.append(ctx.class_definition_src)
    for dep in ctx.dependency_srcs:
        parts.append(dep)
    return "\n\n".join(parts) if parts else "(no additional dependencies)"


def _format_imports(ctx: DependencyContext) -> str:
    return "\n".join(ctx.imports) if ctx.imports else ""


# ──────────────────────────────────────────────────────────────────────────────
# Initial prompt
# ──────────────────────────────────────────────────────────────────────────────

INITIAL_PROMPT_TEMPLATE = """\
**Function under Test**
{function_src}

**Relevant Information from the entire project**
{deps_src}

**The Target code unit you need to cover**
{target_src}

To reach the target code, the test case needs to satisfy conditions along the path:
{constraints_text}

**The most Path-Similar test case**
{proximal_src}

**Path Divergence Analysis**
{divergence_text}

**Your task**
{task_instructions}"""

TASK_INSTRUCTIONS = """\
Create a test case that targets the branch containing our target code.
Use the reference test case as guidance and complete the function body only.
** Important: Only provide the completed test case starting from "class Test" line. Do not include import statements. **
```python
# necessary import statements
class Test(unittest.TestCase):
    @timeout_decorator.timeout(1)
    def test_case_XX(self):
        \"\"\"complete the test case here\"\"\"
        ...
```"""


def build_initial_prompt(
    ctx: DependencyContext,
    target_path: TargetPath,
    proximal: Optional[PathProximalTest],
) -> str:
    """
    Build the initial generation prompt (paper Figure 6).
    """
    unit = ctx.target_unit

    function_src = ctx.enclosing_function_src.strip()
    deps_src = _format_deps(ctx)
    target_src = unit.code_snippet.strip()
    constraints_text = format_constraints(target_path)

    if proximal:
        proximal_src = proximal.test_source.strip()
        divergence_text = format_divergence(proximal)
    else:
        proximal_src = "(no existing test is close to the target path; generate from scratch)"
        divergence_text = "(no divergence analysis available)"

    prompt = INITIAL_PROMPT_TEMPLATE.format(
        function_src=function_src,
        deps_src=deps_src,
        target_src=target_src,
        constraints_text=constraints_text,
        proximal_src=proximal_src,
        divergence_text=divergence_text,
        task_instructions=TASK_INSTRUCTIONS,
    )
    return prompt.strip()


# ──────────────────────────────────────────────────────────────────────────────
# Repair prompt (compilation / runtime errors)
# ──────────────────────────────────────────────────────────────────────────────

REPAIR_PROMPT_TEMPLATE = """\
{initial_prompt}

**The Generated Test Case (FAILED)**
```python
{failed_test}
```

**Error Message**
```
{error_message}
```

**Your task**
{repair_instructions}"""

def _repair_instructions(error_type: str) -> str:
    if error_type == "compilation":
        action = "has a compilation error. Please fix the syntax so that it compiles correctly"
    else:
        action = "raised a runtime error. Please fix the logic so that it runs without exceptions"
    return (
        f"The test case above {action} while still covering the target code unit.\n"
        "** Important: Only provide the completed test case starting from \"class Test\" line. "
        "Do not include import statements. **\n"
        "```python\n"
        "# necessary import statements\n"
        "class Test(unittest.TestCase):\n"
        "    @timeout_decorator.timeout(1)\n"
        "    def test_case_XX(self):\n"
        "        \"\"\"complete the test case here\"\"\"\n"
        "        ...\n"
        "```"
    )


def build_repair_prompt(
    previous_prompt: str,
    previous_test: str,
    error_message: str,
    error_type: str = "compilation",
) -> str:
    """
    Build the repair prompt when a generated test has a compilation or runtime error.

    Parameters
    ----------
    previous_prompt : The initial prompt that produced the failing test.
    previous_test   : Source code of the failing test.
    error_message   : The error string returned by TestExecutor
                      (compilation_error or runtime_error).
    error_type      : "compilation" | "runtime" – controls the repair instruction wording.
    """
    return REPAIR_PROMPT_TEMPLATE.format(
        initial_prompt=previous_prompt.strip(),
        failed_test=previous_test.strip(),
        error_message=error_message.strip(),
        repair_instructions=_repair_instructions(error_type),
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
        f"**Previous Attempt (executed but did not cover the target)**\n"
        f"```python\n{previous_test}\n```\n\n"
        f"The test ran successfully but missed the target code unit.\n"
        f"Updated Path Divergence Analysis based on this new attempt:\n"
        f"{new_div}\n\n"
        f"Please adjust the test inputs / setup to resolve this remaining divergence.\n"
        f"** Important: Respond ONLY with the corrected Python code in backticks. **"
    )
