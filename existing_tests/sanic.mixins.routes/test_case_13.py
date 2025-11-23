import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'Wn-69`lE2__5}?'
            str_1 = '_iO$R,O]'
            tuple_0 = ()
            list_0 = [tuple_0]
            bool_0 = False
            route_mixin_0 = module_0.RouteMixin()
            bool_1 = None
            route_mixin_1 = module_0.RouteMixin()
            var_0 = route_mixin_1.route(str_0, tuple_0, str_1, str_0, list_0, bool_0, bool_1)
            str_2 = 'surrogateescape'
            str_3 = "<ByYpswBG>'XGYaX%!"
            str_4 = 'wzE$_4y\\^D3B'
            list_1 = [str_1, str_2, str_3, str_4]
            var_1 = route_mixin_0.route(str_2, bool_0, bool_0, list_1)
            str_5 = ' u&['
            tuple_1 = ()
            dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_5: tuple_1}
            route_mixin_2 = module_0.RouteMixin(**dict_0)
            dict_1 = {str_5: dict_0, tuple_1: dict_0, str_0: tuple_0, tuple_0: str_1}
            int_0 = -1869
            var_2 = route_mixin_1.add_websocket_route(route_mixin_0, str_0, str_1, dict_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
