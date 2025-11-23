import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 2087
            variable_manager_0 = module_0.VariableManager(int_0)
            var_0 = variable_manager_0.__getstate__()
            bytes_0 = b'P\xea!\x07\xf3\xb7\xc5\x10\x81.\xe0'
            str_0 = '.x\x0cLp\x0b]eW\x0cl$hO"/'
            list_0 = []
            variable_manager_1 = module_0.VariableManager(list_0)
            var_1 = variable_manager_1.set_host_variable(bytes_0, bytes_0, str_0)
            vars_with_sources_0 = module_0.VarsWithSources()
            var_2 = variable_manager_1.__setstate__(vars_with_sources_0)
            bytes_1 = b'Y\x0c\xa0\xd9\xed\x9bl\x85\x91'
            var_3 = variable_manager_1.set_nonpersistent_facts(list_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
