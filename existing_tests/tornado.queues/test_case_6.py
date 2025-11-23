import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = 1412
            queue_0 = module_0.Queue()
            queue_1 = module_0.Queue(int_0)
            int_1 = queue_1.qsize()
            var_0 = None
            timedelta_0 = module_1.timedelta()
            future_0 = queue_1.put(var_0, timedelta_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
