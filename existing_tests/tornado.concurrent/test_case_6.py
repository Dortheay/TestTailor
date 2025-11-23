import unittest
import timeout_decorator
import tornado.concurrent as module_0
import _asyncio as module_1
import builtins as module_2
import concurrent.futures._base as module_3

class Test_Concurrent_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '\n        :arg stream: an `.IOStream`\n        :arg params: a `.HTTP1ConnectionParameters` or None\n        :arg context: an opaque application-defined object that is accessible\n            as ``connection.context``\n        '
            base_exception_0 = module_2.BaseException()
            list_0 = [base_exception_0, str_0, str_0, base_exception_0]
            callable_0 = module_0.run_on_executor(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
