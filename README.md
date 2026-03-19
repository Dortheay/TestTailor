# TestTailor — Code Framework

> **Paper**: *TestTailor: Generating High-Coverage Tests via Path-Proximal Tests with LLMs*
> Zhou et al., FSE 2026

---

## Environment Setup

### Requirements

- Python **3.10+**
- An OpenAI-compatible API key (GPT-4o or DeepSeek-V3)

### Install Dependencies

```bash
# Core dependencies
pip install openai>=1.0.0 coverage>=7.0 timeout-decorator

# Install project in editable mode (optional, for the testtailor entry point)
pip install -e .
```

### API Key Configuration

```bash
export OPENAI_API_KEY="..."
export OPENAI_API_BASE="..."   # set to provider's base URL if not using OpenAI
```

---

## Usage

All commands are run from the **project root** directory.

### Command Line

```bash
python main.py \
    --module  path/to/module.py \
    --tests   path/to/initial_tests/ \
    --project path/to/project_root \
    --model   <model-name> \
    --output  testtailor_output/
```

**Full argument reference:**

| Argument | Default | Description |
|---|---|---|
| `--module` | *(required)* | Python module to improve coverage for |
| `--tests` | *(required)* | Directory of initial test files (`test_*.py` or `*_test.py`) |
| `--project` | *(required)* | Project root (used for cross-file dependency resolution) |
| `--model` | `gpt-4o-2024-11-20` | LLM model name |
| `--max-iter` | `3` | Max repair iterations per uncovered unit |
| `--output` | `testtailor_output/` | Directory to write generated tests |
| `--verbose` | off | Enable debug logging |

### Worked Example (built-in sample)

The repo includes the `order_management` sample project under `tests/order_management/`:

```bash
# Run TestTailor on the OrderService module using its existing test suite
python main.py \
    --module  tests/order_management/service/order_service.py \
    --tests   tests/order_management/tests/ \
    --project tests/order_management/ \
    --output  testtailor_output/
```

### Python API

```python
from main import run_testtailor
from config import TestTailorConfig

config = TestTailorConfig(
    llm_model="gpt-4o-2024-11-20",   # or any OpenAI-compatible model name
    max_iterations_per_unit=3,
    output_dir="testtailor_output/",
)

result = run_testtailor(
    module_path="tests/order_management/service/order_service.py",
    test_dir="tests/order_management/tests/",
    project_root="tests/order_management/",
    config=config,
)

print(f"Coverage: {result.initial_statement_coverage:.1f}% → {result.final_statement_coverage:.1f}%")
print(f"LLM calls: {result.llm_calls}, cost: ${result.api_cost_usd:.4f}")
```

### Output

After a run, `--output` contains:

```
testtailor_output/
└── generated_tests.py    # all coverage-improving tests merged into one file
```

The `generation_test_output/` directory in the repo is an example of the intermediate
artifacts produced during a run:

```
generation_test_output/
├── 01_initial_prompt.txt          # prompt sent to LLM for initial generation
├── 02_failed_test.py              # LLM output that had a syntax error
├── 03_repair_prompt.txt           # repair prompt (includes error + failed test)
└── proximal_tests/
    └── test_nested_branch_small.py   # the path-proximal test used as reference
```

---

## Architecture

```
.
├── main.py                    # Entry point — orchestrates the 3-stage pipeline
├── config.py                  # TestTailorConfig dataclass
├── models.py                  # Shared data models (CodeUnit, TargetPath, …)
│
├── preprocessing/             # ── STAGE 1: Contextual Pre-Processing ──────────
│   ├── unit_partition.py      #   Partition uncovered code → CodeUnit list
│   └── dependency_collector.py#   Backward slicing → DependencyContext
│
├── path_analysis/             # ── STAGE 2: Fine-Grained Path Analysis ─────────
│   ├── cfg_builder.py         #   Build CFG + Dominator Tree from AST
│   ├── symbolic_executor.py   #   Extract PathConstraints (loop hints, elif pruning)
│   ├── path_proximal.py       #   Algorithm 1 — find most path-proximal test
│   └── path_divergence.py     #   Locate first divergence point
│
├── generation/                # ── STAGE 3: Iterative Coverage Improvement ──────
│   ├── llm_client.py          #   OpenAI / DeepSeek API wrapper
│   ├── prompt_builder.py      #   Assemble Figure-6 prompt from all components
│   ├── initial_prompt_builder.py
│   ├── repair_prompt_builder.py
│   └── iterative_generator.py #   generate → execute → repair/refine loop
│
├── execution/                 # ── Test Execution Infrastructure ────────────────
│   ├── trace_collector.py     #   sys.settrace-based runtime path collector
│   └── test_executor.py       #   Isolated subprocess runner + coverage measurement
│
├── utils/
│   └── coverage_utils.py      #   Statement / branch coverage helpers
│
└── tests/                     # Example projects for manual testing
    ├── order_management/      #   Multi-module Python project (service/repo/controller)
    ├── sample_target.py       #   Simple single-function targets
    └── sample_target_v2.py
```

---

## Three-Stage Pipeline

### Stage 1 — Contextual Pre-Processing

**`preprocessing/unit_partition.py`**
Walks every function's AST body and splits uncovered lines into *units*:
- **linear** — consecutive statements with no branching
- **branch** — minimal `if/for/while/try` without deeply nested sub-conditionals

**`preprocessing/dependency_collector.py`**
For each unit:
1. Extracts the enclosing function + class source
2. Runs backward program slicing from all names used in the unit
3. Follows `import` statements across files to collect cross-module dependencies

---

### Stage 2 — Fine-Grained Path Analysis

**`path_analysis/cfg_builder.py`**
Builds a CFG from the function's AST and computes the dominator tree using the
iterative Cooper-Harvey-Kennedy algorithm.

**`path_analysis/symbolic_executor.py`**
Builds the *target path template* by tracing AST upward from the unit to the
function root, then extracts `PathConstraint`s with two special treatments:
- **Loop-aware hints** — records loop guard + iteration count needed
- **Elif-chain pruning** — negates earlier arms so only the intended arm is selected

**`path_analysis/path_proximal.py`** (Algorithm 1)
Hierarchical search on the dominator tree:
1. Sibling-level search — tests covering a sibling branch of the target
2. Ancestor fallback — ascend until a candidate is found
3. Rank by Jaccard(execution_path, target_path); break ties by suffix length

**`path_analysis/path_divergence.py`**
Walks both the target sequence and the proximal test's actual trace in parallel
to find the first line that the proximal test misses, then maps back to source.

---

### Stage 3 — Iterative Coverage Improvement

**`generation/prompt_builder.py`**
Assembles the Figure-6 prompt:
```
Function under Test          ← Stage 1
Relevant Project Context     ← Stage 1
Target Code Unit             ← Stage 1
Symbolic Constraints         ← Stage 2
Path-Proximal Test Case      ← Stage 2
Path Divergence Analysis     ← Stage 2
Formatting / Task            ← fixed template
```
Produces three prompt types: `initial`, `repair` (error), `refine` (missed coverage).

**`generation/iterative_generator.py`**
For each unit, up to `max_iterations_per_unit = 3`:
1. Call LLM → extract code block
2. Execute in subprocess
3. **Covers target** → done ✓
4. **Compilation/runtime error** → `build_repair_prompt` → retry
5. **Runs but misses** + reaches function → elevate to new proximal seed → `build_refine_prompt`
6. **Runs but misses** + doesn't reach function → discard → retry with original prompt

---

## Key Data Models (`models.py`)

| Model | Description |
|---|---|
| `CodeUnit` | One partitioned uncovered execution unit |
| `DependencyContext` | All dependency info for a unit (for the LLM prompt) |
| `PathConstraint` | One symbolic condition along the target path |
| `TargetPath` | Path template + list of `PathConstraint`s |
| `ExecutionPath` | Actual runtime trace of one test case |
| `PathProximalTest` | Selected proximal test + divergence info |
| `GeneratedTest` | LLM-produced test + execution results |
| `ModuleResult` | Final summary for the whole module |

---

## Configuration (`config.py`)

Key fields in `TestTailorConfig`:

| Field | Default | Description |
|---|---|---|
| `llm_model` | `gpt-4o-2024-11-20` | LLM model name |
| `llm_temperature` | `1.0` | Sampling temperature |
| `llm_max_tokens` | `4096` | Max tokens per LLM response |
| `api_key` | `$OPENAI_API_KEY` | API key |
| `api_base` | `$OPENAI_API_BASE` | Custom base URL |
| `max_iterations_per_unit` | `3` | Max repair/refine iterations |
| `test_timeout_seconds` | `10` | Per-test execution timeout |
| `max_constraint_depth` | `10` | Max nesting depth for symbolic constraints |
| `output_dir` | `testtailor_output` | Output directory |

---

## Extension Points

| What to extend | Where |
|---|---|
| Richer symbolic execution | `path_analysis/symbolic_executor.py` — `_collect_constraints` |
| Interprocedural constraints | `preprocessing/dependency_collector.py` — `BackwardSlicer._search_imports` |
| Better loop count estimation | `path_analysis/symbolic_executor.py` — `_estimate_loop_iterations` |
| Support for pytest-style tests | `execution/test_executor.py` — `_RUNNER_SCRIPT` |
| Branch coverage measurement | `execution/test_executor.py` — `measure_coverage` |
| Different LLM providers | `generation/llm_client.py` — add new pricing + base URL |
