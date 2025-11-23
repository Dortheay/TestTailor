import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            float_0 = 2225.2
            queue_0 = module_0.Queue()
            awaitable_0 = queue_0.get(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
