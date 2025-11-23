import unittest
import timeout_decorator
import sanic.mixins.middleware as module_0

class Test_Middleware_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            middleware_mixin_0 = module_0.MiddlewareMixin()
            var_0 = middleware_mixin_0.on_request()
            middleware_mixin_1 = module_0.MiddlewareMixin()
            var_1 = middleware_mixin_0.on_response(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
