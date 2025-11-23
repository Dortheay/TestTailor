import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            future_0 = None
            base_exception_0 = module_2.BaseException()
            module_0.future_set_exception_unless_cancelled(future_0, base_exception_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
