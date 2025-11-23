import unittest
import timeout_decorator
import tornado.log as module_0

class Test_Log_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        log_formatter_0 = module_0.LogFormatter()

if __name__ == "__main__":
    unittest.main()
