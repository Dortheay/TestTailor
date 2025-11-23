import unittest
import timeout_decorator
import sanic.mixins.middleware as module_0

class Test_Middleware_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            middleware_mixin_0 = module_0.MiddlewareMixin()
            var_0 = middleware_mixin_0.on_request()
            var_1 = middleware_mixin_0.on_request()
            list_0 = None
            var_2 = middleware_mixin_0.middleware(list_0)
            var_3 = middleware_mixin_0.middleware(var_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
