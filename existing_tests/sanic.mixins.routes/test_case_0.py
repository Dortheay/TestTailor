import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        route_mixin_0 = module_0.RouteMixin()

if __name__ == "__main__":
    unittest.main()
