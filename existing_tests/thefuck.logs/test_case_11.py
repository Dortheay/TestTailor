import unittest
import timeout_decorator
import thefuck.logs as module_0
import datetime as module_1

class Test_Logs_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = b'K\xa8V\xda\xce^\xac\xfaR\xfa\x18'
            var_0 = module_0.configured_successfully(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
