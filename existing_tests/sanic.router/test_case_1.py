import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '|u'
        iterable_0 = None
        dict_0 = {str_0: str_0}
        bool_0 = False
        router_0 = module_0.Router(str_0)
        var_0 = router_0.add(str_0, iterable_0, dict_0, str_0, str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
