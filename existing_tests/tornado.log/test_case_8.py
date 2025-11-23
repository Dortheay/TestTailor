import unittest
import timeout_decorator
import tornado.log as module_0
import logging as module_1

class Test_Log_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '5;A?p&3X'
            optional_0 = None
            any_0 = None
            dict_0 = {any_0: optional_0}
            logger_0 = module_1.Logger(dict_0)
            module_0.enable_pretty_logging(any_0, logger_0)
            bool_0 = False
            log_formatter_0 = module_0.LogFormatter(bool_0)
            str_1 = log_formatter_0.format(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
