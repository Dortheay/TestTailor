import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            int_0 = 2087
            variable_manager_0 = module_0.VariableManager(int_0)
            bytes_0 = b'\xd3\xda\xf8\x89D\xa1\xe3\xba\xd2z'
            bytes_1 = None
            vars_with_sources_0 = module_0.VarsWithSources()
            var_0 = variable_manager_0.set_host_facts(bytes_1, vars_with_sources_0)
            str_0 = '.x\x0cLp\x0b]eW\x0cl$hO"/'
            list_0 = []
            variable_manager_1 = module_0.VariableManager(list_0)
            var_1 = variable_manager_1.set_host_variable(bytes_0, bytes_0, str_0)
            vars_with_sources_1 = module_0.VarsWithSources()
            var_2 = vars_with_sources_0.copy()
            var_3 = variable_manager_1.__setstate__(vars_with_sources_1)
            str_1 = 'Z=&(,\nZFzo|fOvWPI5'
            str_2 = ' L=\nH=\rE_a\nol'
            dict_0 = {str_1: variable_manager_1, str_2: variable_manager_1}
            str_3 = ')3\x0ceESptdr?c\\:\\^B'
            var_4 = variable_manager_1.set_host_facts(dict_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
