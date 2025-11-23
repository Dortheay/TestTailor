import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        queue_0 = module_0.Queue()
        bool_0 = queue_0.empty()
        int_0 = queue_0.qsize()
        var_0 = None
        queue_0.put_nowait(var_0)
        lifo_queue_0 = module_0.LifoQueue()
        queue_1 = module_0.Queue()
        bool_1 = queue_1.empty()
        int_1 = queue_0.qsize()
        queue_2 = module_0.Queue(int_0)
        var_1 = queue_0.__aiter__()
        var_2 = queue_2.__aiter__()
        queue_3 = module_0.Queue()
        var_3 = queue_0.get_nowait()
        var_4 = queue_2.__aiter__()
        str_0 = queue_1.__repr__()
        queue_0.put_nowait(var_3)
        str_1 = queue_1.__str__()
        queue_4 = module_0.Queue()
        queue_5 = module_0.Queue()
        queue_0.task_done()

if __name__ == "__main__":
    unittest.main()
