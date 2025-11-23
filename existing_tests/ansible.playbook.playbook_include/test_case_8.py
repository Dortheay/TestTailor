import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        playbook_include_0 = module_0.PlaybookInclude()

if __name__ == "__main__":
    unittest.main()
