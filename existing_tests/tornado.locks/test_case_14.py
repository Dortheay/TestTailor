import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        event_0 = module_0.Event()
        event_0.clear()
        event_0.set()

if __name__ == "__main__":
    unittest.main()
