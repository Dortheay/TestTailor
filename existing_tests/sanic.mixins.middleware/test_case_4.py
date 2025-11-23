import unittest
import timeout_decorator
import sanic.mixins.middleware as module_0

class Test_Middleware_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        middleware_mixin_0 = module_0.MiddlewareMixin()
        var_0 = middleware_mixin_0.on_request()

if __name__ == "__main__":
    unittest.main()
