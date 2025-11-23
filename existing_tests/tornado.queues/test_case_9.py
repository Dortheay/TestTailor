import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            queue_full_0 = module_0.QueueFull()
            queue_0 = module_0.Queue()
            str_0 = queue_0.__str__()
            priority_queue_0 = module_0.PriorityQueue()
            timedelta_0 = module_1.timedelta()
            lifo_queue_0 = module_0.LifoQueue()
            queue_1 = module_0.Queue()
            var_0 = queue_1.get_nowait()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
