import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'EH<\rBW'
        releasing_context_manager_0 = module_0._ReleasingContextManager(str_0)
        releasing_context_manager_0.__enter__()
        lock_0 = module_0.Lock()

if __name__ == "__main__":
    unittest.main()
