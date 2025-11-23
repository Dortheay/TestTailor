import unittest
import timeout_decorator
import tornado.queues as module_0

class Test_Queues_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        queue_0 = module_0.Queue()
        int_0 = queue_0.qsize()
        var_0 = None
        queue_0.put_nowait(var_0)
        lifo_queue_0 = module_0.LifoQueue()
        queue_1 = module_0.Queue()
        bool_0 = queue_1.empty()
        int_1 = 206
        int_2 = queue_0.qsize()
        queue_2 = module_0.Queue(int_0)
        var_1 = queue_0.__aiter__()
        var_2 = queue_2.__aiter__()
        queue_3 = module_0.Queue(int_0)
        queue_3.put_nowait(var_0)
        var_3 = queue_2.__aiter__()
        queue_4 = module_0.Queue()
        var_4 = queue_3.get_nowait()
        var_5 = queue_0.__aiter__()
        str_0 = queue_0.__repr__()
        queue_4.put_nowait(var_4)
        queue_5 = module_0.Queue(int_1)
        queue_6 = module_0.Queue()
        queue_3.task_done()

if __name__ == "__main__":
    unittest.main()
