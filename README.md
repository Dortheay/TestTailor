# TestTailor

## Citation

```bibtex
@article{zhou2026testtailor,
    title={TestTailor: Generating High-Coverage Tests via Path-Proximal Tests with LLMs},
    author={Zhou, Xiaoxuan and Lou, Yiling and Dong, Jinhao and Hao, Dan},
    journal={Proc. ACM Softw. Eng.},
    volume={3},
    number={FSE},
    year={2026},
    publisher={ACM},
    doi={10.1145/3797140}
}
```

## Environment Setup

Requires Python 3.10+ and an OpenAI-compatible API key.

```bash
pip install openai>=1.0.0 coverage>=7.0 timeout-decorator
pip install -e .

export OPENAI_API_KEY="..."
export OPENAI_API_BASE="..."   # optional, for non-OpenAI providers
```

## Usage

```bash
python main.py \
    --module  path/to/module.py \
    --tests   path/to/initial_tests/ \
    --project path/to/project_root \
    --output  testtailor_output/
```

Arguments:

- `--module`: target Python module
- `--tests`: directory of initial test files
- `--project`: project root
- `--model`: LLM model name (default `gpt-4o-2024-11-20`)
- `--max-iter`: max repair iterations per unit (default `3`)
- `--output`: output directory (default `testtailor_output/`)

Generated tests are written to `<output>/generated_tests.py`.
