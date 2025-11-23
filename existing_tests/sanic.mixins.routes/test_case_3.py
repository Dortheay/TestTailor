import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = ''
        route_mixin_0 = module_0.RouteMixin()
        int_0 = 1556
        route_mixin_1 = module_0.RouteMixin()
        var_0 = route_mixin_1.patch(str_0, route_mixin_0, int_0)
        str_1 = 'IQ#}gBK&Ib|88}'
        int_1 = 510
        var_1 = route_mixin_1.post(str_1, str_1, int_1)

if __name__ == "__main__":
    unittest.main()
