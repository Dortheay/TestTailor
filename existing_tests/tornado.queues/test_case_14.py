import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        queue_0 = module_0.Queue()

if __name__ == "__main__":
    unittest.main()
