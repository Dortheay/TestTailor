import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            object_dict_0 = module_0.ObjectDict()
            str_0 = 'https'
            object_dict_0.__setattr__(str_0, object_dict_0)
            gzip_decompressor_0 = module_0.GzipDecompressor()
            bytes_0 = b'\xc6\nk\x1a\xec#\xbb\xe9'
            bytes_1 = gzip_decompressor_0.decompress(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
