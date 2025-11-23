import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = ''
            int_0 = None
            list_0 = [int_0, int_0]
            route_mixin_0 = module_0.RouteMixin(*list_0)
            float_0 = 219.147
            dict_0 = None
            bool_0 = False
            var_0 = route_mixin_0.add_route(float_0, str_0, dict_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
