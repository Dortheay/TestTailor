import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            dict_0 = {}
            vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
            dict_1 = None
            var_0 = vars_with_sources_0.__contains__(dict_1)
            var_1 = vars_with_sources_0.__len__()
            variable_manager_0 = module_0.VariableManager()
            variable_manager_1 = module_0.VariableManager()
            vars_with_sources_1 = module_0.VarsWithSources()
            var_2 = vars_with_sources_0.get_source(dict_1)
            var_3 = vars_with_sources_1.copy()
            bool_0 = False
            var_4 = module_0.preprocess_vars(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
