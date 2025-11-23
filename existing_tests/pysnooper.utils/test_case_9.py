import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '\x0bA\x0bNF'
            set_0 = {str_0, str_0, str_0, str_0}
            bool_0 = True
            var_0 = module_0.truncate(set_0, bool_0)
            var_1 = module_0.shitcode(str_0)
            writable_stream_0 = module_0.WritableStream()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
