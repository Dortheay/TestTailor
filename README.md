# TestTailor — Code Framework

> **Paper**: *TestTailor: Generating High-Coverage Tests via Path-Proximal Tests with LLMs*  
> Zhou et al., FSE 2026

---

## Architecture

```
testtailor/
│
├── config.py                  # TestTailorConfig dataclass
├── models.py                  # Shared data models (CodeUnit, TargetPath, …)
├── main.py                    # Entry point — orchestrates the 3-stage pipeline
│
├── preprocessing/             # ── STAGE 1: Contextual Pre-Processing ──────────
│   ├── unit_partition.py      #   Partition uncovered code → CodeUnit list ✅
│   └── dependency_collector.py#   Backward slicing → DependencyContext ✅
│
├── path_analysis/             # ── STAGE 2: Fine-Grained Path Analysis ─────────
│   ├── cfg_builder.py         #   Build CFG + Dominator Tree from AST ✅
│   ├── symbolic_executor.py   #   Extract PathConstraints (loop hints, elif pruning) ✅
│   ├── path_proximal.py       #   Algorithm 1 — find most path-proximal test ✅
│   └── path_divergence.py     #   Locate first divergence point
│
├── generation/                # ── STAGE 3: Iterative Coverage Improvement ──────
│   ├── llm_client.py          #   OpenAI / DeepSeek API wrapper ✅
│   ├── prompt_builder.py      #   Assemble Figure-6 prompt from all components
│   └── iterative_generator.py #   generate → execute → repair/refine loop
│
├── execution/                 # ── Test Execution Infrastructure ────────────────
│   ├── trace_collector.py     #   sys.settrace-based runtime path collector ✅
│   └── test_executor.py       #   Isolated subprocess runner + coverage measurement ✅
│
└── utils/
    └── coverage_utils.py      #   Statement / branch coverage helpers
```

---

## Three-Stage Pipeline

### Stage 1 — Contextual Pre-Processing

**`unit_partition.py`**  
Walks every function's AST body and splits uncovered lines into *units*:
- **linear** — consecutive statements with no branching
- **branch** — minimal `if/for/while/try` without deeply nested sub-conditionals

**`dependency_collector.py`**  
For each unit:
1. Extracts the enclosing function + class source
2. Runs backward program slicing from all names used in the unit
3. Follows `import` statements across files to collect cross-module dependencies

---

### Stage 2 — Fine-Grained Path Analysis

**`cfg_builder.py`**  
Builds a CFG from the function's AST and computes the dominator tree using the
iterative Cooper-Harvey-Kennedy algorithm.

**`symbolic_executor.py`**  
Builds the *target path template* by tracing AST upward from the unit to the
function root, then extracts `PathConstraint`s with two special treatments:
- **Loop-aware hints** — records loop guard + iteration count needed
- **Elif-chain pruning** — negates earlier arms so only the intended arm is selected

**`path_proximal.py`** (Algorithm 1)  
Hierarchical search on the dominator tree:
1. Sibling-level search — tests covering a sibling branch of the target
2. Ancestor fallback — ascend until a candidate is found
3. Rank by Jaccard(execution_path, target_path); break ties by suffix length

**`path_divergence.py`**  
Walks both the target sequence and the proximal test's actual trace in parallel
to find the first line that the proximal test misses, then maps back to source.

---

### Stage 3 — Iterative Coverage Improvement

**`prompt_builder.py`**  
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

**`iterative_generator.py`**  
For each unit, up to `max_iterations_per_unit = 3`:
1. Call LLM → extract code block
2. Execute in subprocess
3. **Covers target** → done ✓
4. **Compilation/runtime error** → `build_repair_prompt` → retry
5. **Runs but misses** + reaches function → elevate to new proximal seed → `build_refine_prompt`
6. **Runs but misses** + doesn't reach function → discard → retry with original prompt

---

## Usage

### Command Line

```bash
export OPENAI_API_KEY="sk-..."           
export OPENAI_API_BASE="https://api.openai.com/v1"  

python -m testtailor.main \
    --module  path/to/module.py \
    --tests   path/to/initial_tests/ \
    --project path/to/project_root \
    --model   gpt-4o-2024-11-20 \
    --max-iter 3 \
    --output  testtailor_output/
```

For DeepSeek-V3:

```bash
export OPENAI_API_KEY="<deepseek-key>"
export OPENAI_API_BASE="https://api.deepseek.com"

python -m testtailor.main \
    --module  path/to/module.py \
    --tests   path/to/initial_tests/ \
    --project path/to/project_root \
    --model   deepseek-chat
```

### Python API

```python
from testtailor import TestTailorConfig, run_testtailor

# 推荐：依赖环境变量 OPENAI_API_KEY / OPENAI_API_BASE
config = TestTailorConfig(
    llm_model="gpt-4o-2024-11-20",
    max_iterations_per_unit=3,
)

result = run_testtailor(
    module_path="src/mymodule.py",
    test_dir="tests/",
    project_root=".",
    config=config,
)

print(f"Coverage: {result.initial_statement_coverage:.1f}% → {result.final_statement_coverage:.1f}%")
print(f"LLM calls: {result.llm_calls}, cost: ${result.api_cost_usd:.4f}")
```

---

## Installation

```bash
pip install openai coverage
# optional: pip install pytest pytest-cov

# install testtailor in editable mode
pip install -e .
```

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

## Extension Points

| What to extend | Where |
|---|---|
| Richer symbolic execution | `path_analysis/symbolic_executor.py` — `_collect_constraints` |
| Interprocedural constraints | `preprocessing/dependency_collector.py` — `BackwardSlicer._search_imports` |
| Better loop count estimation | `symbolic_executor.py` — `_estimate_loop_iterations` |
| Support for pytest-style tests | `execution/test_executor.py` — `_RUNNER_SCRIPT` |
| Branch coverage measurement | `execution/test_executor.py` — `measure_coverage` |
| Different LLM providers | `generation/llm_client.py` — add new pricing + base URL |
