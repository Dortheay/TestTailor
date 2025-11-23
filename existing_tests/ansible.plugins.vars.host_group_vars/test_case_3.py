import unittest
import timeout_decorator
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.group as module_1
import ansible.inventory.host as module_2

class Test_Host_group_vars_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            vars_module_0 = module_0.VarsModule()
            vars_module_1 = module_0.VarsModule()
            vars_module_2 = module_0.VarsModule()
            tuple_0 = ()
            int_0 = 1731
            host_0 = module_2.Host(tuple_0)
            var_0 = vars_module_0.get_vars(tuple_0, int_0, host_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
