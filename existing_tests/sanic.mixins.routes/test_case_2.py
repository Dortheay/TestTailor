import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'cu'
        dict_0 = {str_0: str_0}
        bool_0 = True
        route_mixin_0 = module_0.RouteMixin()
        var_0 = route_mixin_0.route(str_0, dict_0, bool_0)

if __name__ == "__main__":
    unittest.main()
