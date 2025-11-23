import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            list_0 = []
            dict_0 = {}
            ansible_j2_vars_0 = module_0.AnsibleJ2Vars(bool_0, list_0, dict_0)
            ansible_j2_vars_1 = module_0.AnsibleJ2Vars(ansible_j2_vars_0, dict_0)
            var_0 = ansible_j2_vars_1.__iter__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
