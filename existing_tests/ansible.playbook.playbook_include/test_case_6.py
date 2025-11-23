import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'import_playbook'
            str_1 = 'vars'
            str_2 = 'playbook.yml'
            str_3 = 'key'
            str_4 = {str_3: str_2}
            str_5 = {str_0: str_2, str_1: str_4}
            playbook_include_0 = module_0.PlaybookInclude()
            playbook_include_1 = module_0.PlaybookInclude()
            var_0 = playbook_include_1.preprocess_data(str_5)
            list_0 = [str_1, str_0, str_3]
            ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject()
            float_0 = 74.9859
            var_1 = playbook_include_1.load_data(list_0, ansible_base_y_a_m_l_object_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
