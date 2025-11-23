import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            type_0 = None
            int_0 = 570
            router_0 = module_0.Router(type_0, int_0)
            str_0 = None
            float_0 = -4493.0
            float_1 = 15.0
            dict_0 = {int_0: router_0, router_0: str_0, type_0: float_0, type_0: type_0}
            tuple_0 = (float_0, float_1, dict_0)
            float_2 = None
            bool_0 = True
            bool_1 = False
            bool_2 = True
            var_0 = router_0.add(str_0, tuple_0, float_2, bool_0, bool_1, bool_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
