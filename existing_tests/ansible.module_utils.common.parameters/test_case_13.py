import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            var_0 = module_0.env_fallback()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
