import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            future_0 = None
            bool_0 = False
            dummy_executor_0 = module_0.DummyExecutor()
            dummy_executor_0.shutdown(bool_0)
            str_0 = ''
            list_0 = [str_0, str_0, str_0]
            return_value_ignored_error_0 = module_0.ReturnValueIgnoredError(*list_0)
            return_value_ignored_error_1 = module_0.ReturnValueIgnoredError()
            list_1 = [str_0]
            callable_0 = module_0.run_on_executor(*list_1)
            var_0 = None
            module_0.future_set_result_unless_cancelled(future_0, var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
