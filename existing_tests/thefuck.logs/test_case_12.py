import unittest
import timeout_decorator
import thefuck.logs as module_0
import datetime as module_1

class Test_Logs_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            float_0 = 869.3
            complex_0 = None
            var_0 = module_0.how_to_configure_alias(complex_0)
            bytes_0 = b'w'
            bool_0 = False
            var_1 = module_0.version(bytes_0, bool_0, float_0)
            var_2 = module_0.how_to_configure_alias(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
