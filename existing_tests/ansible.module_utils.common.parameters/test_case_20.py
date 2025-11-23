import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'TEST_VAR'
            str_1 = 'TEST_ENV_2'
            list_0 = [str_1, str_0, str_1]
            var_0 = module_0.env_fallback(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
