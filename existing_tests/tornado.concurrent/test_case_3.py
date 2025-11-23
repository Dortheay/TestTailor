import unittest
import timeout_decorator
import tornado.concurrent as module_0
import concurrent.futures._base as module_1

class Test_Concurrent_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        callable_0 = module_0.run_on_executor()
        future_0 = module_1.Future()
        str_0 = 'Ty'
        module_0.future_set_result_unless_cancelled(future_0, str_0)

if __name__ == "__main__":
    unittest.main()
