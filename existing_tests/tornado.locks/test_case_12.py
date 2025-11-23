import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        lock_0 = module_0.Lock()

if __name__ == "__main__":
    unittest.main()
