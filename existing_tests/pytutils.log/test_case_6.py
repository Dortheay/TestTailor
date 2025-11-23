import unittest
import timeout_decorator
import pytutils.log as module_0

class Test_Log_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            float_0 = 108.0
            var_0 = module_0.get_logger(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
