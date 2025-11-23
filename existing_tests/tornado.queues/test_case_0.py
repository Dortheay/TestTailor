import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            queue_full_0 = module_0.QueueFull()
            queue_iterator_0 = module_0._QueueIterator(dict_0)
            queue_0 = module_0.Queue()
            str_0 = queue_0.__repr__()
            awaitable_0 = queue_iterator_0.__anext__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
