import unittest
import timeout_decorator
import sanic.mixins.middleware as module_0

class Test_Middleware_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'K'
        bytes_0 = b'\xea\xc2\x96D\x0e\xc1'
        middleware_mixin_0 = module_0.MiddlewareMixin()
        var_0 = middleware_mixin_0.middleware(str_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
