import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            future_0 = module_3.Future()
            float_0 = 292.00635
            module_0.future_add_done_callback(future_0, float_0)
            callable_0 = module_0.run_on_executor()
            callable_1 = module_0.run_on_executor()
            return_value_ignored_error_0 = module_0.ReturnValueIgnoredError()
            var_0 = None
            return_value_ignored_error_1 = module_0.ReturnValueIgnoredError()
            float_1 = None
            bool_0 = module_0.is_future(float_1)
            list_0 = []
            base_exception_0 = module_2.BaseException(*list_0)
            module_0.future_set_exception_unless_cancelled(future_0, base_exception_0)
            module_0.future_set_result_unless_cancelled(future_0, var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
