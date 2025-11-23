import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            float_0 = 1962.45
            playbook_include_0 = module_0.PlaybookInclude()
            var_0 = playbook_include_0.load(bool_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
