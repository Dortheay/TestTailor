import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()

if __name__ == "__main__":
    unittest.main()
