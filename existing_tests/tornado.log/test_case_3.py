import unittest
import timeout_decorator
import tornado.log as module_0
import logging as module_1

class Test_Log_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = None
            tuple_0 = (list_0,)
            module_0.define_logging_options(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
