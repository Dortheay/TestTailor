import unittest
import timeout_decorator
import tornado.concurrent as module_0
import concurrent.futures._base as module_1

class Test_Concurrent_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        callable_0 = module_0.run_on_executor()
        dummy_executor_0 = module_0.DummyExecutor()
        int_0 = None
        future_0 = dummy_executor_0.submit(int_0)

if __name__ == "__main__":
    unittest.main()
