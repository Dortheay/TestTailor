import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = "$5tm8g;'{\t^+-|0"
        bool_0 = False
        route_mixin_0 = module_0.RouteMixin()
        var_0 = route_mixin_0.get(str_0, str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
