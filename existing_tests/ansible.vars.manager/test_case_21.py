import unittest
import timeout_decorator
import ansible.vars.manager as module_0
import builtins as module_1

class Test_Manager_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dict_0 = None
        var_0 = module_0.preprocess_vars(dict_0)

if __name__ == "__main__":
    unittest.main()
