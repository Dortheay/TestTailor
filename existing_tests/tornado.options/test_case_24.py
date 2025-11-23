import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = 'bHrEWPv*1|te8],~'
            iterator_0 = None
            module_0.define(str_0, iterator_0)
            option_parser_0 = module_0.OptionParser()
            str_1 = '-h;HNr3B"'
            dict_0 = option_parser_0.group_dict(str_1)
            option_parser_0.run_parse_callbacks()
            set_0 = option_parser_0.groups()
            type_0 = module_1.type()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
