import unittest
import timeout_decorator
import thefuck.logs as module_0
import datetime as module_1

class Test_Logs_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            var_0 = module_0.already_configured(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
