import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            semaphore_0 = module_0.Semaphore()
            semaphore_0.release()
            event_0 = module_0.Event()
            semaphore_0.__aenter__()
            timeout_garbage_collector_0 = module_0._TimeoutGarbageCollector()
            condition_0 = module_0.Condition()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
