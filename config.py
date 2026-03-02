"""
TestTailor Configuration
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TestTailorConfig:
    # LLM settings
    llm_model: str = "gpt-4o-2024-11-20"
    llm_temperature: float = 1.0
    llm_max_tokens: int = 4096
    api_key: Optional[str] = None
    api_base: Optional[str] = None  # for DeepSeek or custom endpoints

    # Execution settings
    max_iterations_per_unit: int = 3       # max repair iterations per uncovered unit
    test_timeout_seconds: int = 10         # per-test execution timeout
    initial_run_minutes: int = 2           # CODAMOSA warm-up time
    max_run_minutes: int = 20              # total budget per module

    # Coverage settings
    coverage_tool: str = "coverage"        # Python coverage package

    # Path analysis settings
    max_constraint_depth: int = 10         # max nesting depth for symbolic constraints
    max_loop_unroll: int = 5              # max iterations hint for loops

    # Output settings
    output_dir: str = "testtailor_output"
    verbose: bool = True
