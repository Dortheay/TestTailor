import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            semaphore_0 = module_0.Semaphore()
            base_exception_0 = module_1.BaseException()
            str_0 = '}{yH&vJCs2\x0c$4:\r<9'
            semaphore_0.__exit__(semaphore_0, base_exception_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
