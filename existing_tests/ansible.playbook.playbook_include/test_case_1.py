import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            set_0 = set()
            playbook_include_0 = module_0.PlaybookInclude()
            var_0 = playbook_include_0.load(dict_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
