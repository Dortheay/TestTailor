import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            lock_0 = module_0.Lock()
            lock_0.release()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
