import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            future_0 = module_3.Future()
            base_exception_0 = None
            module_0.future_set_exception_unless_cancelled(future_0, base_exception_0)
            str_0 = '=+D'
            none_type_0 = None
            float_0 = 907.697
            tuple_0 = (str_0, none_type_0, float_0)
            bool_0 = module_0.is_future(tuple_0)
            future_1 = None
            module_0.future_set_exc_info(future_1, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
