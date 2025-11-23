import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        queue_empty_0 = module_0.QueueEmpty()

if __name__ == "__main__":
    unittest.main()
