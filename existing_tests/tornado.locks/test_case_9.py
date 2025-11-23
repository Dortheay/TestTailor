import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            awaitable_0 = None
            base_exception_0 = module_1.BaseException()
            semaphore_0 = module_0.Semaphore()
            lock_0 = module_0.Lock()
            lock_0.__aexit__(awaitable_0, base_exception_0, semaphore_0)
            event_0 = module_0.Event()
            event_0.set()
            event_0.set()
            awaitable_1 = event_0.wait()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
