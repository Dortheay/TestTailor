# TestTailor Replication Package v1.0


## Installation

```bash
pip install coverage pytest openai
```
Note: `ast` is a built-in Python module, no installation needed.

## Quick Start

### Step 0: The replication data of our experiments

Due to the substantial size of the dataset, we have hosted the replication package on Google Drive. We strictly adhere to the double-blind policy: this link is configured for anonymous access, ensuring mutual anonymity—authors cannot track reviewer access, and reviewers cannot see author identities. The only name within the drive has been replaced with pseudonyms.

Please refer to [Google Drive](https://drive.google.com/drive/folders/1qOk1eci-FWaScBsWI6rgaBGDTe2QMQXh?usp=sharing)

### Step 1: Coverage Analysis

Analyze your project to identify uncovered code blocks:

```bash
python CoverageAnalyzer.py <src_dir> <test_dir> --output coverage_report.json --suggestions test_suggestions.json
```

- `src_dir`: Source code directory
- `test_dir`: Existing test directory
- `--output`: Coverage report output file (default: `coverage_report.json`)
- `--suggestions`: Test suggestions output file (default: `test_suggestions.json`)

### Step 2: Similarity Analysis

Run existing tests and analyze similarity with uncovered code:

```bash
python testcaseRecoder.py <src_dir> <test_dir> --output test_results --suggestions test_suggestions.json --analyze-similarity
```

This generates `similarity_analysis.json` containing similarity scores between uncovered code and existing test cases.

### Step 3: Generate Test Cases

Use the LLM generator to create test cases:

```python
from testGenerator import LLMTestGenerator
from pathlib import Path
import json

# Initialize generator
generator = LLMTestGenerator(
    api_key="YOUR_API_KEY",
    target_module_path="/path/to/project/target_module.py",
    api_base="https://api.example.com/v1"  # Optional: custom API endpoint
)

# Load similarity analysis results
group_list = generator.parse_line_numbers_from_similarity_json(
    "/path/to/project/similarity_analysis.json",
    "target_file.py"
)

# Generate tests for each group
project_dir = Path("/path/to/project")
test_dir = Path("/path/to/project/tests")
output_dir = "/path/to/project/generated_tests"

for group in group_list:
    record = generator.generate_tests(
        group, 
        project_dir, 
        test_dir, 
        output_dir, 
        num_attempts=3
    )
    # Save generation record
    with open("generation_records.jsonl", 'a') as f:
        f.write(json.dumps(record) + '\n')
```

## Configuration

### API Setup

Configure your LLM API in `testGenerator.py`:

- `api_key`: Your API key
- `api_base`: API endpoint URL (default: `https://api.example.com/v1`)
- `model_name`: Model to use (default: `gpt-4o-2024-11-20`)
- `temperature`: Generation temperature (default: `1.0`)
- `max_retries`: Maximum retry attempts (default: `2`)

### Coverage Settings

The system uses `coverage` library for coverage analysis. Configure in `CoverageAnalyzer.py`:

- Source directories
- Omit patterns (e.g., `*/tmp*.py`, `*/__pycache__/*`)

## Workflow

```
Source Code
    ↓
[Static Analysis] → Code structure, execution paths, path constraints
    ↓
[Coverage Analysis] → Uncovered code blocks → test_suggestions.json
    ↓
[Similarity Analysis] → Path-proximal test cases → similarity_analysis.json
    ↓
[LLM Generation] → Generate test code → Execute & validate
    ↓
[Iterative Refinement] → Fix errors / improve coverage 
    ↓
Final Test Cases
```

## Key Features

- **Path-based Generation**: Uses static analysis to ensure generated tests cover target code paths
- **Similarity-guided**: Leverages existing test cases as references
- **Iterative Refinement**: Automatically fixes errors and improves coverage
- **Incremental Coverage**: Considers tests successful if they add new coverage

## Output Files

- `coverage_report.json`: Coverage statistics and analysis
- `test_suggestions.json`: Uncovered code blocks with path constraints
- `similarity_analysis.json`: Similarity scores and reference test cases
- `generation_records.jsonl`: Detailed generation logs for each test case
- Generated test files: Saved in the specified output directory

## Requirements

- Python 3.8+
- coverage
- pytest
- openai

## Notes

- Ensure your project structure is compatible with the coverage tool
- Test directories should follow standard naming conventions (`test_*.py`)
- The system requires existing test cases for similarity analysis
- API costs depend on the number of LLM calls and token usage

## Example

See `useTestGenerator.py` for a complete example of the generation workflow.
