import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            router_0 = module_0.Router(bool_0)
            str_0 = '\n|'
            int_0 = 1008
            callable_0 = None
            var_0 = router_0.add(str_0, int_0, callable_0, str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
