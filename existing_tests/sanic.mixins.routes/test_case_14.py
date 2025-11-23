import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '\x0c6Mel'
            bool_0 = True
            bool_1 = True
            list_0 = [bool_1, bool_1, bool_1, bool_1]
            route_mixin_0 = module_0.RouteMixin(*list_0)
            var_0 = route_mixin_0.get(str_0, str_0, bool_0)
            str_1 = None
            dict_0 = {}
            route_mixin_1 = module_0.RouteMixin(**dict_0)
            var_1 = route_mixin_1.static(dict_0, str_1, route_mixin_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
