import unittest
import timeout_decorator
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

class Test_Playbook_include_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'import_playbook'
        str_1 = {str_0: str_0, str_0: str_0}
        playbook_include_0 = module_0.PlaybookInclude()
        playbook_include_1 = module_0.PlaybookInclude()
        var_0 = playbook_include_1.preprocess_data(str_1)
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject()

if __name__ == "__main__":
    unittest.main()
