import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '|h%cJ\n=_L[8'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            playbook_include_0 = module_0.PlaybookInclude()
            bool_0 = False
            var_0 = playbook_include_0.load_data(dict_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
