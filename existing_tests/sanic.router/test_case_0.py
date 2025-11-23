import unittest
import timeout_decorator
import sanic.router as module_0

class Test_Router_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        router_0 = module_0.Router()

if __name__ == "__main__":
    unittest.main()
