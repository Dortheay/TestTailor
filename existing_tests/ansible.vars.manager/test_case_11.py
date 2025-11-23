import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            bool_0 = True
            bool_1 = False
            variable_manager_0 = module_0.VariableManager()
            vars_with_sources_0 = module_0.VarsWithSources()
            var_0 = vars_with_sources_0.get_source(variable_manager_0)
            str_0 = 'N(4\\vwtR'
            dict_0 = {str_0: bool_1, str_0: str_0}
            vars_with_sources_1 = module_0.VarsWithSources(**dict_0)
            variable_manager_1 = module_0.VariableManager()
            var_1 = variable_manager_1.set_nonpersistent_facts(vars_with_sources_1, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
