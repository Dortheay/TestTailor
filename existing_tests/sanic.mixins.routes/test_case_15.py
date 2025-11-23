import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            route_mixin_0 = module_0.RouteMixin()
            pure_path_0 = None
            str_0 = '/]IvQ{IAH]>K|<Myob'
            dict_0 = {}
            route_mixin_1 = module_0.RouteMixin(**dict_0)
            var_0 = route_mixin_1.get(str_0)
            int_0 = 426
            dict_1 = {}
            str_1 = ";'1X0I$"
            bool_0 = True
            int_1 = None
            route_mixin_2 = module_0.RouteMixin()
            var_1 = route_mixin_2.patch(str_1, str_1, bool_0, int_1)
            route_mixin_3 = module_0.RouteMixin()
            route_mixin_4 = module_0.RouteMixin()
            str_2 = 'W4{'
            route_mixin_5 = module_0.RouteMixin()
            str_3 = '\tP9.D&'
            bool_1 = True
            var_2 = route_mixin_2.route(str_3, dict_1, int_0, bool_1)
            var_3 = route_mixin_3.delete(str_2, int_0)
            var_4 = route_mixin_4.static(int_0, pure_path_0, int_0, dict_1, route_mixin_2, route_mixin_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
