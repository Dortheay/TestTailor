import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'slgL\x0b'
            iterable_0 = None
            str_1 = None
            bool_0 = False
            bool_1 = True
            list_0 = []
            str_2 = 'g]4*|g>4l%N>[/7=t'
            tuple_0 = (str_2,)
            bool_2 = False
            router_0 = module_0.Router(list_0, tuple_0, bool_2)
            var_0 = router_0.add(str_0, iterable_0, str_1, str_0, bool_0, bool_0, str_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
