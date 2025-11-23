import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '79DCvL,r'
            str_1 = module_0.fwd_normalize_address(str_0)
            int_0 = 25
            tuple_0 = (str_1, int_0)
            dict_0 = module_0.fwd_normalize(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
