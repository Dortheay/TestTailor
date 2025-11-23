import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 406
            str_0 = ' b>M:RL8\x0c%~s_/WK'
            str_1 = ''
            str_2 = 'websocket_handshake'
            set_0 = set()
            route_mixin_0 = module_0.RouteMixin()
            var_0 = route_mixin_0.websocket(str_1, str_2, set_0)
            dict_0 = {}
            route_mixin_1 = module_0.RouteMixin(**dict_0)
            bool_0 = True
            var_1 = route_mixin_1.get(str_0)
            bool_1 = True
            var_2 = route_mixin_1.websocket(str_0, int_0, bool_1)
            str_3 = 's#e5f9Vst^6AcWE]@'
            var_3 = route_mixin_1.post(str_3, str_2)
            var_4 = route_mixin_1.options(str_0, bool_0, str_0)
            str_4 = 'wJJ!wuaTh@2'
            list_0 = []
            bool_2 = True
            tuple_0 = (list_0, bool_2)
            var_5 = route_mixin_0.add_websocket_route(tuple_0, str_4, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
