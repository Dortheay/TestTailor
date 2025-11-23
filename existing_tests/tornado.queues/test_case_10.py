import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            queue_0 = module_0.Queue()
            str_0 = queue_0.__repr__()
            str_1 = queue_0.__str__()
            queue_1 = module_0.Queue()
            bool_0 = queue_0.empty()
            int_0 = queue_1.qsize()
            int_1 = None
            lifo_queue_0 = module_0.LifoQueue(int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
