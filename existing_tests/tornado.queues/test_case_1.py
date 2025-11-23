import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -3417
            queue_0 = module_0.Queue(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
