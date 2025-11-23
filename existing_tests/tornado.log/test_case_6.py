import unittest
import timeout_decorator
import tornado.log as module_0
import logging as module_1

class Test_Log_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'\x964%\x12\x86\xb3\x86\x0e\x04: \xb2\x15\xbf@\xe8x_'
            module_0.enable_pretty_logging(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
