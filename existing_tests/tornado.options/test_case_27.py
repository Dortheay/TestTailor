import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            str_0 = "F\nA\nd'%Z"
            dict_0 = {str_0: str_0}
            str_1 = 'ji;PV{6>0M'
            tuple_0 = ()
            option_0 = module_0._Option(str_1, str_1, tuple_0)
            option_0.set(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
