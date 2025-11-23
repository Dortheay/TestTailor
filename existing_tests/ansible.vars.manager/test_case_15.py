import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            bool_0 = False
            bool_1 = False
            dict_0 = {bool_0: bool_0, bool_1: bool_0}
            variable_manager_0 = module_0.VariableManager()
            var_0 = variable_manager_0.set_nonpersistent_facts(bool_1, dict_0)
            vars_with_sources_0 = module_0.VarsWithSources()
            var_1 = module_0.preprocess_vars(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
