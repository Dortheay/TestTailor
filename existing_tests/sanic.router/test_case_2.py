import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        type_0 = None
        str_0 = ';qm<\\'
        bool_0 = False
        router_0 = module_0.Router(str_0, bool_0, type_0)
        float_0 = 5009.29508
        iterable_0 = None
        str_1 = ': '
        bool_1 = False
        bool_2 = True
        var_0 = router_0.add(str_0, iterable_0, str_1, iterable_0, bool_1, bool_2, str_1)
        router_1 = module_0.Router(str_0, float_0)
        var_1 = router_0.finalize()
        router_2 = module_0.Router(router_1)

if __name__ == "__main__":
    unittest.main()
