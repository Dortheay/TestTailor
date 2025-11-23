import unittest
import timeout_decorator
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.group as module_1
import ansible.inventory.host as module_2

class Test_Host_group_vars_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 69
            bytes_0 = b'^'
            vars_module_0 = module_0.VarsModule()
            var_0 = vars_module_0.get_vars(int_0, bytes_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
