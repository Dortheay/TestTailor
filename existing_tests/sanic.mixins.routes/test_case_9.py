import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = 345
            dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
            str_0 = ' found.\n  Example File: project/sanic_server.py -> app\n  Example Module: project.sanic_server.app'
            route_mixin_0 = module_0.RouteMixin()
            var_0 = route_mixin_0.add_websocket_route(dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
