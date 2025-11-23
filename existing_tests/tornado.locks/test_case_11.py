import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        event_0 = module_0.Event()

if __name__ == "__main__":
    unittest.main()
