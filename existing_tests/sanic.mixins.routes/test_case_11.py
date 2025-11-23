import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            route_mixin_0 = module_0.RouteMixin()
            str_0 = None
            str_1 = '-'
            dict_0 = {str_1: str_1}
            bool_0 = True
            var_0 = route_mixin_0.delete(str_0, dict_0, str_1, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
