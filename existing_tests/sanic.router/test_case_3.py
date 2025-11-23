import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        router_0 = module_0.Router()
        str_0 = 'routes_all'
        var_0 = hasattr(router_0, str_0)
        str_1 = 'routes_static'
        var_1 = hasattr(router_0, str_1)
        var_2 = hasattr(router_0, str_1)
        str_2 = 'routes_regex'
        var_3 = hasattr(router_0, str_2)
        str_3 = 'name_index'
        var_4 = hasattr(router_0, str_3)

if __name__ == "__main__":
    unittest.main()
