import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = "pR.Y Rp~_'"
            iterable_0 = None
            float_0 = 3.1734642339658787
            bool_0 = True
            bool_1 = True
            router_0 = module_0.Router(str_0, float_0, bool_0, bool_1)
            var_0 = router_0.add(str_0, iterable_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
