import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            bool_1 = False
            variable_manager_0 = module_0.VariableManager()
            var_0 = variable_manager_0.clear_facts(bool_1)
            list_0 = [bool_0]
            var_1 = module_0.preprocess_vars(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
