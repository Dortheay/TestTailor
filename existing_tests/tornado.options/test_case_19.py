import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = ''
            str_1 = 'RH-+9eQ'
            list_0 = [str_1, str_1]
            option_0 = module_0._Option(str_1, list_0, str_1)
            any_0 = option_0.parse(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
