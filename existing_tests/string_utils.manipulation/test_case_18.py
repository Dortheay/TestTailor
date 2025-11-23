import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            float_0 = 3953.99893
            dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
            string_formatter_0 = module_0.__StringFormatter(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
