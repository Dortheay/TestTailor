import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'l_'
            float_0 = None
            dict_0 = {str_0: float_0}
            str_1 = 'l'
            float_1 = 1181.66
            ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_1, float_1)
            var_0 = ansible_j2_vars_0.add_locals(dict_0)
            set_0 = set()
            list_0 = None
            ansible_j2_vars_1 = module_0.AnsibleJ2Vars(set_0, list_0)
            var_1 = ansible_j2_vars_1.__len__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
