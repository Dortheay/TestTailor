import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            int_0 = 2087
            variable_manager_0 = module_0.VariableManager(int_0)
            var_0 = variable_manager_0.__getstate__()
            bool_0 = False
            variable_manager_1 = module_0.VariableManager(bool_0)
            var_1 = variable_manager_1.__getstate__()
            str_0 = 'M0MG'
            bytes_0 = b'P\xea!\x07\xf3\xb7\xc5\x10\x81.\xe0'
            str_1 = '.x\x0cLp\x0b]eW\x0cl$hO"/'
            var_2 = variable_manager_1.set_host_variable(bytes_0, bytes_0, str_1)
            vars_with_sources_0 = module_0.VarsWithSources()
            var_3 = variable_manager_1.__setstate__(vars_with_sources_0)
            vars_with_sources_1 = module_0.VarsWithSources()
            str_2 = "rd '2\r8%zQ%)~"
            str_3 = 'Bw</nX'
            dict_0 = {str_2: str_2, str_3: str_0}
            var_4 = variable_manager_1.set_nonpersistent_facts(vars_with_sources_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
