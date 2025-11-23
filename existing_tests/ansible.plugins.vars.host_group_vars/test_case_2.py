import unittest
import timeout_decorator
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.group as module_1
import ansible.inventory.host as module_2

class Test_Host_group_vars_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            vars_module_0 = module_0.VarsModule()
            vars_module_1 = module_0.VarsModule()
            group_0 = module_1.Group()
            var_0 = vars_module_1.get_vars(group_0, vars_module_1, group_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
