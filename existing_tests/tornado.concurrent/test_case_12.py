import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            dummy_executor_0 = module_0.DummyExecutor()
            list_0 = [dummy_executor_0, dummy_executor_0, dummy_executor_0, dummy_executor_0]
            str_0 = 'semaphore initial value must be >= 0'
            dict_0 = {str_0: str_0}
            callable_0 = module_0.run_on_executor(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
