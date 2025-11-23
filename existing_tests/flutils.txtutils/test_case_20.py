import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
        int_0 = module_0.len_without_ansi(str_0)
        str_1 = 'hello'
        int_1 = module_0.len_without_ansi(str_1)
        str_2 = '\x1b[38;5;209mfoo'
        str_3 = 'bar\x1b[0m'
        str_4 = 'baz'
        str_5 = [str_2, str_3, str_4]
        int_2 = module_0.len_without_ansi(str_5)
        str_6 = ''
        int_3 = module_0.len_without_ansi(str_6)
        str_7 = '\x1b[38;5;209m'
        int_4 = module_0.len_without_ansi(str_7)
        str_8 = '\x1b[38;5;209mfoo\x1b[invalidmbar\x1b[0mbaz'
        int_5 = module_0.len_without_ansi(str_8)

if __name__ == "__main__":
    unittest.main()
