"""
Shared data models for TestTailor.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Set
import ast


@dataclass
class CodeUnit:
    """
    Represents the smallest contiguous execution unit of uncovered code.
    A unit is either a linear sequence of statements or a minimal branching
    construct (e.g., a simple if without nested conditionals).
    """
    unit_id: str                        # unique identifier e.g. "func_name:unit_0"
    source_file: str                    # path to the source file
    function_name: str                  # enclosing function name
    start_lineno: int                   # first line of the unit
    end_lineno: int                     # last line of the unit
    unit_type: str                      # "linear" | "branch" | "loop"
    branch_condition: Optional[str] = None   # condition text if unit_type == "branch"
    code_snippet: str = ""              # raw source text of the unit
    ast_node: Optional[ast.AST] = None  # AST node for the unit (not serialized)

    def __repr__(self):
        return (f"CodeUnit({self.unit_id}, lines {self.start_lineno}-{self.end_lineno}, "
                f"type={self.unit_type})")


@dataclass
class DependencyContext:
    """
    All dependency information collected for a CodeUnit,
    ready to be inserted into the LLM prompt.
    """
    target_unit: CodeUnit
    enclosing_function_src: str         # source of the function containing the unit
    class_definition_src: Optional[str] = None   # class def + __init__ if applicable
    dependency_srcs: List[str] = field(default_factory=list)  # other funcs/classes/vars
    imports: List[str] = field(default_factory=list)          # relevant import lines


@dataclass
class PathConstraint:
    """
    A single symbolic constraint extracted along the target path.
    """
    condition: str          # the Boolean expression, e.g. "not isinstance(config, dict)"
    negated: bool = False   # True if we need the False branch
    constraint_type: str = "branch"   # "branch" | "loop_entry" | "loop_count" | "elif"
    loop_count_hint: Optional[int] = None   # for loops: how many iterations needed
    lineno: int = 0


@dataclass
class TargetPath:
    """
    The path template from function entry to the target uncovered unit.
    Not a concrete execution trace – a structural skeleton.
    """
    unit: CodeUnit
    constraints: List[PathConstraint] = field(default_factory=list)
    path_nodes: List[int] = field(default_factory=list)  # linenos of decision points


@dataclass
class ExecutionPath:
    """
    The actual execution path of a single test case (collected at runtime).
    """
    test_id: str
    test_source: str                    # raw Python source of the test
    covered_lines: Set[int] = field(default_factory=set)
    visited_nodes: List[int] = field(default_factory=list)  # ordered CFG node ids
    reached_function: bool = False
    exception_info: Optional[str] = None


@dataclass
class PathProximalTest:
    """
    The selected path-proximal test case and its analysis results.
    """
    test_id: str
    test_source: str
    execution_path: ExecutionPath
    jaccard_similarity: float
    divergence_lineno: Optional[int] = None       # first line where paths diverge
    divergence_condition: Optional[str] = None    # condition text at divergence
    target_continues_to: Optional[str] = None     # what the target path does after
    proximal_continues_to: Optional[str] = None   # what this test does after


@dataclass
class GeneratedTest:
    """
    A test case produced by the LLM and its evaluation results.
    """
    unit_id: str
    iteration: int
    source: str                         # full Python source of the test
    executed: bool = False
    compilation_error: Optional[str] = None
    runtime_error: Optional[str] = None
    newly_covered_lines: Set[int] = field(default_factory=set)
    covers_target: bool = False         # True if target unit is fully covered
    reaches_function: bool = False      # True if test at least enters the function


@dataclass
class ModuleResult:
    """
    Final result for one Python module.
    """
    module_path: str
    initial_statement_coverage: float
    initial_branch_coverage: float
    final_statement_coverage: float
    final_branch_coverage: float
    generated_tests: List[GeneratedTest] = field(default_factory=list)
    llm_calls: int = 0
    api_cost_usd: float = 0.0
