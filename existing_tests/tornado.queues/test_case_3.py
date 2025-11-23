import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            queue_0 = module_0.Queue()
            str_0 = queue_0.__repr__()
            str_1 = queue_0.__str__()
            queue_1 = module_0.Queue()
            bool_0 = queue_0.empty()
            var_0 = queue_0.get_nowait()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
