import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            bool_1 = False
            router_0 = module_0.Router(bool_0, bool_1)
            var_0 = router_0.finalize()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
