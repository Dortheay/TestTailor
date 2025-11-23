import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = 'uYX!b70P+mbx\\s'
            str_1 = module_0.snake_case_to_camel(str_0)
            str_2 = module_0.prettify(str_0)
            str_3 = module_0.reverse(str_0)
            string_compressor_0 = module_0.__StringCompressor()
            str_4 = '#/GrFG\x0b2RKih)s6Gc3'
            bool_0 = module_0.booleanize(str_4)
            string_formatter_0 = module_0.__StringFormatter(str_1)
            str_5 = string_formatter_0.format()
            str_6 = None
            str_7 = module_0.strip_html(str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
