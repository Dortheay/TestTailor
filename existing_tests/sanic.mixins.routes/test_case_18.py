import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            int_0 = 406
            str_0 = ' b>M:RL8\x0c%~s_/WK'
            dict_0 = {}
            route_mixin_0 = module_0.RouteMixin(**dict_0)
            bool_0 = True
            var_0 = route_mixin_0.websocket(str_0, str_0, bool_0)
            str_1 = 's#e5f9Vst^6AcWE]@'
            var_1 = route_mixin_0.post(str_1, str_1)
            route_mixin_1 = module_0.RouteMixin()
            var_2 = route_mixin_1.websocket(str_0, bool_0)
            var_3 = route_mixin_0.options(str_0, bool_0, str_0)
            str_2 = 'wJJ!wuaTh@2'
            str_3 = 'oO\\{@'
            list_0 = []
            var_4 = route_mixin_0.add_route(str_2, str_3, list_0, str_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
