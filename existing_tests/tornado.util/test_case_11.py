import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            tuple_0 = ()
            str_0 = '\r{9z~9'
            str_1 = '~'
            str_2 = 'qE\t1!)&XkM?>u\tVds6"'
            str_3 = '0Pc?'
            dict_0 = {str_0: tuple_0, str_1: str_1, str_2: tuple_0, str_3: str_2}
            str_4 = 'aJ[['
            int_0 = 595
            module_0.exec_in(str_4, dict_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
