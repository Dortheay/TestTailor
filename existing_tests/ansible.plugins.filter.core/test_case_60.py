import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_61(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        float_0 = 100.0
        var_0 = module_0.from_yaml_all(float_0)

if __name__ == "__main__":
    unittest.main()
