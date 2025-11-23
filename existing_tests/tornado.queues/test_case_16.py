import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        var_0 = None
        queue_0 = module_0.Queue()
        queue_0.put_nowait(var_0)
        int_0 = 65535
        queue_1 = module_0.Queue(int_0)

if __name__ == "__main__":
    unittest.main()
