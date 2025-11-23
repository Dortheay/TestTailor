import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            tuple_0 = None
            bool_0 = False
            variable_manager_0 = module_0.VariableManager()
            variable_manager_1 = module_0.VariableManager()
            var_0 = variable_manager_1.set_host_variable(tuple_0, bool_0, variable_manager_0)
            variable_manager_2 = module_0.VariableManager()
            int_0 = 131072
            str_0 = 'eAp`@'
            var_1 = variable_manager_1.get_vars(int_0, bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
