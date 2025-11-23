import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            module_0.print_help()
            str_0 = "F\nA\x0b\nd'%Z"
            option_parser_0 = module_0.OptionParser()
            mockable_0 = module_0._Mockable(option_parser_0)
            list_0 = [str_0, str_0]
            list_1 = module_0.parse_command_line(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
