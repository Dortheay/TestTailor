import unittest
import timeout_decorator
import tornado.concurrent as module_0
import concurrent.futures._base as module_1

class Test_Concurrent_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        callable_0 = module_0.run_on_executor()

if __name__ == "__main__":
    unittest.main()
