import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            base_exception_0 = module_1.BaseException()
            semaphore_0 = module_0.Semaphore()
            semaphore_0.__enter__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
