import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            str_0 = '6Hj`'
            int_0 = 2087
            variable_manager_0 = module_0.VariableManager(int_0)
            var_0 = variable_manager_0.__getstate__()
            str_1 = 'M0MG'
            dict_0 = {str_0: str_1, str_0: variable_manager_0}
            vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
            var_1 = vars_with_sources_0.__len__()
            var_2 = variable_manager_0.__getstate__()
            bytes_0 = b'\xd3\xda\xf8\x89D\xa1\xe3\xba\xd2z'
            bytes_1 = b'P\xea!\x07\xf3\xb7\xc5\x10\x81.\xe0'
            list_0 = []
            var_3 = variable_manager_0.set_nonpersistent_facts(bytes_0, vars_with_sources_0)
            variable_manager_1 = module_0.VariableManager(list_0)
            var_4 = variable_manager_1.set_host_variable(bytes_1, bytes_1, str_0)
            vars_with_sources_1 = module_0.VarsWithSources()
            vars_with_sources_2 = module_0.VarsWithSources(*list_0)
            var_5 = variable_manager_1.__setstate__(vars_with_sources_1)
            str_2 = 'Z=&(,\nZFzo|fOvWPI5'
            bool_0 = None
            set_0 = {str_0, variable_manager_0, str_2, bool_0}
            var_6 = variable_manager_1.set_host_facts(bytes_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
