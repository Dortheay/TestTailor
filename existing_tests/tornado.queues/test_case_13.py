import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = None
        queue_iterator_0 = module_0._QueueIterator(var_0)

if __name__ == "__main__":
    unittest.main()
