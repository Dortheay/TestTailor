import unittest
import timeout_decorator
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

class Test_Locks_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            float_0 = 634.274
            releasing_context_manager_0 = module_0._ReleasingContextManager(float_0)
            releasing_context_manager_0.__enter__()
            dict_0 = {releasing_context_manager_0: releasing_context_manager_0}
            base_exception_0 = None
            optional_0 = None
            releasing_context_manager_0.__exit__(dict_0, base_exception_0, optional_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
