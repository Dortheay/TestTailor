import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -3238
            semaphore_0 = module_0.Semaphore()
            semaphore_0.release()
            semaphore_1 = module_0.Semaphore(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
