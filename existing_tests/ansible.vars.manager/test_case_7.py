import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '/proc/cmdline'
            variable_manager_0 = module_0.VariableManager(str_0)
            vars_with_sources_0 = module_0.VarsWithSources()
            str_1 = ''
            str_2 = 'module_util_paths'
            dict_0 = {str_1: vars_with_sources_0, str_2: variable_manager_0}
            variable_manager_1 = module_0.VariableManager()
            var_0 = variable_manager_1.set_host_variable(variable_manager_0, vars_with_sources_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
