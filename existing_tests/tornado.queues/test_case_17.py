import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = 4115
        queue_0 = module_0.Queue(int_0)
        str_0 = queue_0.__repr__()
        var_0 = queue_0.__aiter__()

if __name__ == "__main__":
    unittest.main()
