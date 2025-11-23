import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        router_0 = module_0.Router()
        str_0 = 'routes_all'
        var_0 = hasattr(router_0, str_0)
        str_1 = 'routes_static'
        var_1 = hasattr(router_0, str_1)
        str_2 = 'routes_dynamic'
        var_2 = hasattr(router_0, str_2)
        str_3 = 'routes_regex'
        var_3 = hasattr(router_0, str_3)
        str_4 = 'ctx'
        var_4 = hasattr(router_0, str_4)

if __name__ == "__main__":
    unittest.main()
