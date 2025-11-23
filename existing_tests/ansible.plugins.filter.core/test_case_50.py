import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_51(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -2103
        var_0 = module_0.to_yaml(int_0)

if __name__ == "__main__":
    unittest.main()
