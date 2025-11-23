import unittest
import timeout_decorator
import semantic_release.settings as module_0

class Test_Settings_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = -2768
        var_0 = module_0.overload_configuration(int_0)

if __name__ == "__main__":
    unittest.main()
