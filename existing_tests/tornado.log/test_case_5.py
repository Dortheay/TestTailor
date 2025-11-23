import unittest
import timeout_decorator
import tornado.log as module_0
import logging as module_1

class Test_Log_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            module_0.enable_pretty_logging()
            module_0.define_logging_options()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
