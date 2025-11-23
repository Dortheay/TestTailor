import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'import_playbook'
            str_1 = 'key'
            str_2 = 'value'
            str_3 = {str_1: str_2}
            str_4 = {str_0: str_3, str_0: str_3}
            playbook_include_0 = module_0.PlaybookInclude()
            var_0 = playbook_include_0.preprocess_data(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
