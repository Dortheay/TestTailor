import unittest
import timeout_decorator
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1

class Test_Host_group_vars_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'h^$JK\r_+Op'
        host_0 = module_1.Host(str_0)
        bool_0 = False
        vars_module_0 = module_0.VarsModule()
        var_0 = vars_module_0.get_vars(host_0, bool_0, host_0)

if __name__ == "__main__":
    unittest.main()
