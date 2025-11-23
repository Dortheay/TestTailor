import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 406
            dict_0 = {}
            route_mixin_0 = module_0.RouteMixin()
            route_mixin_1 = module_0.RouteMixin(**dict_0)
            str_0 = 'wJY!wuxTh12'
            list_0 = []
            var_0 = route_mixin_1.add_route(str_0, str_0, list_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
