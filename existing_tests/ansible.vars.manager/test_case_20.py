import unittest
import timeout_decorator
import ansible.vars.manager as module_0
import builtins as module_1

class Test_Manager_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        variable_manager_0 = module_0.VariableManager()

if __name__ == "__main__":
    unittest.main()
