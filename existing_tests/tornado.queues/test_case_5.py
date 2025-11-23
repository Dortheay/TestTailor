import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            queue_0 = module_0.Queue()
            bool_0 = queue_0.full()
            queue_1 = module_0.Queue()
            queue_1.task_done()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
