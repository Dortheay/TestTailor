import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 1416.88
            str_0 = ''
            bool_0 = False
            bool_1 = True
            route_mixin_0 = module_0.RouteMixin()
            var_0 = route_mixin_0.add_route(float_0, str_0, bool_0, str_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
