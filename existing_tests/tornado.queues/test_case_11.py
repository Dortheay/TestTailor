import unittest
import timeout_decorator
import tornado.queues as module_0
import datetime as module_1

class Test_Queues_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            queue_0 = module_0.Queue()
            str_0 = queue_0.__repr__()
            queue_1 = module_0.Queue()
            bool_0 = queue_0.empty()
            int_0 = queue_1.qsize()
            var_0 = None
            queue_1.put_nowait(var_0)
            lifo_queue_0 = module_0.LifoQueue()
            queue_2 = module_0.Queue()
            bool_1 = queue_2.empty()
            int_1 = queue_1.qsize()
            queue_3 = module_0.Queue(int_0)
            var_1 = queue_1.__aiter__()
            queue_4 = module_0.Queue()
            var_2 = queue_1.get_nowait()
            var_3 = queue_1.__aiter__()
            str_1 = queue_1.__repr__()
            queue_3.put_nowait(var_2)
            queue_5 = module_0.Queue()
            int_2 = 3149
            queue_6 = module_0.Queue(int_2)
            queue_0.task_done()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
