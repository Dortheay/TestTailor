import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = '!au\x0bo0>[c\r)TyL'
        bool_0 = False
        str_1 = 'c'
        str_2 = '1X+Mg\tqW^5K=-\x0b'
        dict_0 = {str_1: str_1, str_2: str_2}
        route_mixin_0 = module_0.RouteMixin(**dict_0)
        var_0 = route_mixin_0.head(str_0, bool_0, bool_0)

if __name__ == "__main__":
    unittest.main()
