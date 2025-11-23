import unittest
import timeout_decorator
import tornado.locks as module_0

class Test_Locks_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        event_0 = module_0.Event()
        str_0 = event_0.__repr__()

if __name__ == "__main__":
    unittest.main()
