import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = 'foobar'
        int_0 = module_0.len_without_ansi(str_0)
        str_1 = '\x1b[38;5;209mfoobar\x1b[0m'
        int_1 = module_0.len_without_ansi(str_1)
        str_2 = 'foo\x1b[31mbar\x1b[0m'
        int_2 = module_0.len_without_ansi(str_2)
        str_3 = ''
        int_3 = module_0.len_without_ansi(str_3)
        str_4 = 'foo'
        str_5 = 'bar'
        str_6 = [str_4, str_5]
        int_4 = module_0.len_without_ansi(str_6)
        str_7 = '\x1b[31mbar\x1b[0m'
        str_8 = [str_4, str_7]
        int_5 = module_0.len_without_ansi(str_8)
        str_9 = '\x1b[31foo'
        int_6 = module_0.len_without_ansi(str_9)

if __name__ == "__main__":
    unittest.main()
