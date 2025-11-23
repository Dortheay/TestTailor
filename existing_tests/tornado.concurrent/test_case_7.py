import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            future_0 = None
            module_0.chain_future(future_0, future_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
