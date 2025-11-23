import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'vars'
            str_1 = 'value'
            str_2 = {str_1: str_0, str_0: str_1}
            playbook_include_0 = module_0.PlaybookInclude()
            var_0 = playbook_include_0.preprocess_data(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
