import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            list_0 = []
            variable_manager_0 = module_0.VariableManager()
            dict_0 = {}
            vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
            var_0 = vars_with_sources_0.copy()
            var_1 = variable_manager_0.__setstate__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
