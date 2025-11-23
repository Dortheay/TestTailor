import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = '6Hj`'
            dict_0 = {str_0: str_0, str_0: str_0}
            int_0 = 2087
            int_1 = -742
            dict_1 = {str_0: int_0, str_0: dict_0, str_0: int_0, str_0: int_1}
            list_0 = [str_0, str_0]
            bytes_0 = b'#\xf8U\x8b\x8f\xbb\xbb\x98'
            bool_0 = True
            tuple_0 = (list_0, bytes_0, bool_0)
            variable_manager_0 = module_0.VariableManager(tuple_0)
            var_0 = variable_manager_0.set_inventory(dict_1)
            variable_manager_1 = module_0.VariableManager(int_0)
            var_1 = variable_manager_1.__getstate__()
            bytes_1 = None
            vars_with_sources_0 = module_0.VarsWithSources()
            var_2 = variable_manager_1.set_host_facts(bytes_1, vars_with_sources_0)
            bytes_2 = b'P\xea!\x07\xf3\xb7\xc5\x10\x81.\xe0'
            str_1 = '.x\x0cLp\x0b]eW\x0cl$hO"/'
            list_1 = []
            variable_manager_2 = module_0.VariableManager(list_1)
            var_3 = variable_manager_2.set_host_variable(bytes_2, bytes_2, str_1)
            vars_with_sources_1 = module_0.VarsWithSources()
            var_4 = vars_with_sources_0.copy()
            var_5 = variable_manager_2.__setstate__(vars_with_sources_1)
            str_2 = 'Z=&(,\nZFzo|fOvWPI5'
            str_3 = ' L=\nH=\rE_a\nol'
            dict_2 = {str_2: variable_manager_2, str_3: var_1}
            var_6 = variable_manager_1.set_host_facts(dict_2, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
