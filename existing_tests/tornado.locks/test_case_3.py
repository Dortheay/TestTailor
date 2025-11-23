import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            lock_0 = module_0.Lock()
            awaitable_0 = lock_0.acquire()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
