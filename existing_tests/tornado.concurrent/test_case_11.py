import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            future_0 = module_3.Future()
            dict_0 = {}
            bytes_0 = b'='
            str_0 = '7, 8, 13'
            dummy_executor_0 = module_0.DummyExecutor()
            future_1 = dummy_executor_0.submit(str_0)
            module_0.future_set_result_unless_cancelled(future_0, bytes_0)
            base_exception_0 = module_2.BaseException(**dict_0)
            return_value_ignored_error_0 = module_0.ReturnValueIgnoredError()
            str_1 = '/me'
            float_0 = 808.401621
            list_0 = []
            dummy_executor_1 = module_0.DummyExecutor()
            future_2 = dummy_executor_1.submit(float_0, *list_0)
            str_2 = '^R2}L_6y#,\\\tD!DjT'
            dict_1 = {str_1: future_0, str_1: base_exception_0, str_1: dict_0, str_2: dict_0}
            module_0.future_add_done_callback(future_0, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
