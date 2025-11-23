import unittest
import timeout_decorator
import ansible.modules.slurp as module_0

class Test_Slurp_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.main()

if __name__ == "__main__":
    unittest.main()
