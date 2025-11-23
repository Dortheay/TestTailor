import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 1423
        priority_queue_0 = module_0.PriorityQueue(int_0)

if __name__ == "__main__":
    unittest.main()
