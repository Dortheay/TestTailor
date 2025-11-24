from testGenerator import LLMTestGenerator
from pathlib import Path
import os
import sys
import json

llmgenerator = LLMTestGenerator(api_key="YOUR_API_KEY", target_module_path="/path/to/project/target_module.py")
group_list = llmgenerator.parse_line_numbers_from_similarity_json("/path/to/project/similarity_analysis.json", "target_file.py")
project_dir = Path("/path/to/project")
test_dir = Path("/path/to/project/tests")
output_dir = "/path/to/project/generated_tests"
target_root = os.path.abspath('/path/to/project')
if target_root not in sys.path:
    sys.path.insert(0, target_root) 
output_file = os.path.join(output_dir, "all_generation_records_parser.jsonl")
llmgenerator.coverage_trace_log_path = os.path.join(output_dir, "llm_call_vs_coverage.jsonl")

for i, group in enumerate(group_list):
    print("The current group is " + str(group))
    currentrecord = llmgenerator.generate_tests(group, project_dir, test_dir, output_dir, 3)

    with open(output_file, 'a', encoding='utf-8') as f:
        json_line = json.dumps(currentrecord, ensure_ascii=False)
        f.write(json_line + '\n')
            
    print(f"Completed group {i+1}/{len(group_list)}")
    
print(f"All tests completed, results saved to {output_file}")

try:
        sys.path.remove(target_root)
except ValueError:
        pass
        