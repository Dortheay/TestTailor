import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            lock_0 = module_0.Lock()
            event_0 = module_0.Event()
            int_0 = 913
            semaphore_0 = module_0.Semaphore(int_0)
            str_0 = ''
            lock_0.__exit__(semaphore_0, semaphore_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
