import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            iterable_0 = None
            str_0 = '_/.iP(8Pu{l'
            tuple_0 = module_0.parse_host(str_0)
            str_1 = module_0.fwd_normalize_address(str_0)
            dict_0 = module_0.fwd_normalize(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
