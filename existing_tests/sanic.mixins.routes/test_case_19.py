import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = 406
            str_0 = ''
            str_1 = 'websocket_handshake'
            set_0 = set()
            route_mixin_0 = module_0.RouteMixin()
            var_0 = route_mixin_0.websocket(str_0, str_1, set_0)
            dict_0 = {}
            route_mixin_1 = module_0.RouteMixin(**dict_0)
            bool_0 = True
            var_1 = route_mixin_1.get(str_1)
            bool_1 = True
            var_2 = route_mixin_1.websocket(str_0, int_0, bool_1)
            str_2 = 's#e5f9Vst^6AcWE]@'
            var_3 = route_mixin_1.post(str_2, str_1)
            var_4 = route_mixin_1.options(str_0, bool_0, str_0)
            str_3 = 'wJJ!wuaTh@2'
            str_4 = 'oO\\{@'
            list_0 = []
            str_5 = None
            int_1 = None
            var_5 = route_mixin_1.add_route(str_3, str_4, list_0, str_5, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
