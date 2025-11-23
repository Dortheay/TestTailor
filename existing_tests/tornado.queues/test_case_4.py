import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 2
            queue_0 = module_0.Queue(int_0)
            int_1 = 1
            queue_0.put_nowait(int_1)
            int_2 = queue_0.qsize()
            queue_0.put_nowait(int_0)
            bool_0 = queue_0.full()
            int_3 = 3
            queue_0.put_nowait(int_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
