import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'p&'
            variable_manager_0 = module_0.VariableManager()
            str_1 = ''
            str_2 = '*Hk|'
            dict_0 = {str_1: str_0, str_2: str_0, str_1: str_2, str_2: str_2}
            vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
            var_0 = vars_with_sources_0.__iter__()
            str_3 = 'q~;SWU.EShq'
            var_1 = variable_manager_0.__setstate__(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
