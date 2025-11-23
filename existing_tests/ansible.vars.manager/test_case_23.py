import unittest
import timeout_decorator
import ansible.vars.manager as module_0
import builtins as module_1

class Test_Manager_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '6Hj`'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.preprocess_vars(dict_0)
        bytes_0 = b'P\xea!\x07\xf3\xb7\xc5\x10\x81.\xe0'
        str_1 = '.x\x0cLp\x0b]eW\x0cl$hO"/'
        list_0 = []
        vars_with_sources_0 = module_0.VarsWithSources(*list_0)
        variable_manager_0 = module_0.VariableManager(list_0)
        var_1 = variable_manager_0.set_host_variable(bytes_0, bytes_0, str_1)
        vars_with_sources_1 = module_0.VarsWithSources()
        vars_with_sources_2 = module_0.VarsWithSources(*list_0)
        var_2 = variable_manager_0.__setstate__(vars_with_sources_1)
        dict_1 = module_1.dict()
        str_2 = 'Bc\t\t'
        var_3 = variable_manager_0.set_host_facts(str_2, dict_1)
        var_4 = vars_with_sources_1.__iter__()

if __name__ == "__main__":
    unittest.main()
