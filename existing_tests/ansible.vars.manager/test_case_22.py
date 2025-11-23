import unittest
import timeout_decorator
import ansible.vars.manager as module_0
import builtins as module_1

class Test_Manager_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'A-\tbn:[me^)_\rqH'
        list_0 = [str_0]
        int_0 = 5986
        str_1 = '1'
        variable_manager_0 = module_0.VariableManager(int_0, str_1)
        int_1 = 60
        variable_manager_1 = module_0.VariableManager(list_0, variable_manager_0, int_1)
        variable_manager_2 = module_0.VariableManager(variable_manager_1)
        var_0 = variable_manager_2.__getstate__()

if __name__ == "__main__":
    unittest.main()
