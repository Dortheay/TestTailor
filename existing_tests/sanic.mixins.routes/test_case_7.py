import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'SlNt<%n|'
            int_0 = 401
            tuple_0 = (int_0,)
            route_mixin_0 = module_0.RouteMixin()
            var_0 = route_mixin_0.static(str_0, str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
