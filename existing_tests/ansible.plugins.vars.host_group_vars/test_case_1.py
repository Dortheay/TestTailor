import unittest
import timeout_decorator
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.group as module_1
import ansible.inventory.host as module_2

class Test_Host_group_vars_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            vars_module_0 = module_0.VarsModule()
            bool_0 = False
            list_0 = [vars_module_0, bool_0, bool_0]
            dict_0 = {vars_module_0: list_0}
            var_0 = vars_module_0.get_vars(bool_0, dict_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
