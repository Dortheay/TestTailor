import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            dict_0 = {}
            route_mixin_0 = module_0.RouteMixin(**dict_0)
            str_0 = 't'
            var_0 = route_mixin_0.add_websocket_route(str_0, str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
