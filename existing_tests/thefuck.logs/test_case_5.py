import unittest
import timeout_decorator
import thefuck.logs as module_0
import datetime as module_1

class Test_Logs_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'm\xed\xfe\x0f\r8\xad\xf3G\xf5\xe8\xdep\xb2'
            bool_0 = None
            list_0 = [bool_0]
            tuple_0 = (bool_0, list_0, bool_0)
            var_0 = module_0.exception(bytes_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
