import unittest
import timeout_decorator
import ansible.vars.manager as module_0
import builtins as module_1

class Test_Manager_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'test_host'
        str_1 = 'test_var'
        str_2 = 'test_value'
        var_0 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
        str_3 = 'key1'
        str_4 = 'value1'
        str_5 = {str_3: str_4}
        var_1 = variable_manager_0.set_host_variable(str_0, str_1, str_5)
        str_6 = 'key2'
        str_7 = 'value2'
        str_8 = {str_6: str_7}
        var_2 = variable_manager_0.set_host_variable(str_0, str_1, str_8)
        var_3 = variable_manager_0._vars_cache[str_0][str_1]

if __name__ == "__main__":
    unittest.main()
