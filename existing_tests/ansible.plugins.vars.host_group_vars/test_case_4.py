import unittest
import timeout_decorator
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1

class Test_Host_group_vars_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        vars_module_0 = module_0.VarsModule()

if __name__ == "__main__":
    unittest.main()
