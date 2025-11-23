import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        lock_0 = module_0.Lock()
        event_0 = module_0.Event()
        releasing_context_manager_0 = module_0._ReleasingContextManager(event_0)
        semaphore_0 = module_0.Semaphore()
        str_0 = semaphore_0.__repr__()
        semaphore_1 = module_0.Semaphore()
        semaphore_1.release()
        event_1 = module_0.Event()
        event_1.set()
        semaphore_2 = module_0.Semaphore()
        str_1 = semaphore_0.__repr__()
        semaphore_3 = module_0.Semaphore()
        semaphore_4 = module_0.Semaphore()
        semaphore_4.release()
        lock_1 = module_0.Lock()
        str_2 = lock_1.__repr__()
        event_2 = module_0.Event()
        event_0.clear()
        str_3 = event_1.__repr__()
        event_3 = module_0.Event()
        event_1.set()

if __name__ == "__main__":
    unittest.main()
