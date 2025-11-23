import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        var_0 = None
        queue_0 = module_0.Queue()
        queue_0.put_nowait(var_0)
        var_1 = None
        queue_iterator_0 = module_0._QueueIterator(var_1)
        var_2 = queue_0.__aiter__()
        var_3 = queue_0.__aiter__()
        queue_1 = module_0.Queue()
        var_4 = queue_0.get_nowait()
        var_5 = queue_0.__aiter__()
        var_6 = queue_1.__aiter__()

if __name__ == "__main__":
    unittest.main()
