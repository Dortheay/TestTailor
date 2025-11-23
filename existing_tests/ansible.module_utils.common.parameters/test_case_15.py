import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 0.001
            list_0 = [float_0, float_0]
            var_0 = module_0.env_fallback(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
