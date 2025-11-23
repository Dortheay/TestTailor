import unittest
import timeout_decorator
import tornado.log as module_0

class Test_Log_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        optional_0 = None
        module_0.enable_pretty_logging(optional_0)

if __name__ == "__main__":
    unittest.main()
