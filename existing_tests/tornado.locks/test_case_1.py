import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            event_0 = module_0.Event()
            event_0.clear()
            event_0.set()
            awaitable_0 = event_0.wait()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
