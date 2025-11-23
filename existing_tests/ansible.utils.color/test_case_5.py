import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        complex_0 = None
        float_0 = -3361.87
        var_0 = module_0.stringc(complex_0, float_0)

if __name__ == "__main__":
    unittest.main()
