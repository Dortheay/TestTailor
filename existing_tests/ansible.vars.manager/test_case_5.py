import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = False
            variable_manager_0 = module_0.VariableManager()
            variable_manager_1 = module_0.VariableManager()
            var_0 = variable_manager_1.clear_facts(bool_0)
            list_0 = []
            var_1 = module_0.preprocess_vars(list_0)
            dict_0 = {}
            bool_1 = False
            bytes_0 = b'D\xa14"\xbd\xd9%\x95\x93\xdd\x85h4\x0e'
            var_2 = variable_manager_0.get_vars(dict_0, bool_1, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
