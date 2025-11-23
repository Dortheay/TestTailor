import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            dict_0 = {}
            variable_manager_0 = module_0.VariableManager()
            var_0 = variable_manager_0.set_inventory(dict_0)
            float_0 = -2235.77
            float_1 = -5802.00947
            variable_manager_1 = module_0.VariableManager(float_1)
            var_1 = variable_manager_1.set_nonpersistent_facts(dict_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
