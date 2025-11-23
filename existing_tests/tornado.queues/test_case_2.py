import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            queue_0 = module_0.Queue()
            var_0 = queue_0.get_nowait()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
