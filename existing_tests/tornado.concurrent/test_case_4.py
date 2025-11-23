import unittest
import timeout_decorator
import tornado.concurrent as module_0
import concurrent.futures._base as module_1

class Test_Concurrent_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        future_0 = module_1.Future()
        base_exception_0 = None
        module_0.future_set_exception_unless_cancelled(future_0, base_exception_0)

if __name__ == "__main__":
    unittest.main()
