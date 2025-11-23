import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dummy_executor_0 = module_0.DummyExecutor()
            dummy_executor_1 = module_0.DummyExecutor()
            dummy_executor_0.shutdown()
            list_0 = [dummy_executor_0, dummy_executor_1, dummy_executor_1]
            tuple_0 = ()
            future_0 = dummy_executor_1.submit(tuple_0)
            str_0 = 'Semaphore'
            bool_0 = None
            dummy_executor_1.shutdown(bool_0)
            float_0 = -4624.36
            future_1 = dummy_executor_1.submit(float_0)
            dict_0 = {str_0: dummy_executor_0, str_0: dummy_executor_0, str_0: list_0}
            future_2 = module_1.Future(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
