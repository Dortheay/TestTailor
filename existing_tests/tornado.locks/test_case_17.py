import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        semaphore_0 = module_0.Semaphore()
        semaphore_0.release()

if __name__ == "__main__":
    unittest.main()
