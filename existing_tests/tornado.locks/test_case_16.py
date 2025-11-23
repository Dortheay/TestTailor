import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        lock_0 = module_0.Lock()
        str_0 = lock_0.__repr__()

if __name__ == "__main__":
    unittest.main()
