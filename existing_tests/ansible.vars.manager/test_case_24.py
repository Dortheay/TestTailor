import unittest
import timeout_decorator
import ansible.vars.manager as module_0
import builtins as module_1

class Test_Manager_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        bytes_0 = b'P\xea!\x07\xf3\xb7\xc5\x10\x81.\xe0'
        str_0 = '.x\x0cLp\x0b]eW\x0cl$hO"/'
        list_0 = []
        vars_with_sources_0 = module_0.VarsWithSources(*list_0)
        variable_manager_0 = module_0.VariableManager(list_0)
        var_0 = variable_manager_0.set_host_variable(bytes_0, bytes_0, str_0)
        vars_with_sources_1 = module_0.VarsWithSources(*list_0)
        var_1 = variable_manager_0.__setstate__(vars_with_sources_0)
        dict_0 = module_1.dict()
        str_1 = 'Bc\t\t'
        var_2 = variable_manager_0.set_host_facts(str_1, dict_0)
        var_3 = vars_with_sources_0.__iter__()

if __name__ == "__main__":
    unittest.main()
