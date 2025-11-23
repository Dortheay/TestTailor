import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        gzip_decompressor_0 = module_0.GzipDecompressor()

if __name__ == "__main__":
    unittest.main()
