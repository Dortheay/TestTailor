import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            float_0 = 497.0
            float_1 = 619.78823
            variable_manager_0 = module_0.VariableManager()
            var_0 = variable_manager_0.set_host_facts(float_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
