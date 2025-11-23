import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            callable_0 = None
            module_0.add_parse_callback(callable_0)
            option_parser_0 = module_0.OptionParser()
            str_0 = None
            bool_0 = True
            option_parser_0.parse_config_file(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
