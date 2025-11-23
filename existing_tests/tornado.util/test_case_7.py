import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = b'\x1b\x01b+\xf8'
            str_0 = '"|NK:*p4<$!9 a0'
            str_1 = '_'
            list_0 = [bytes_0, str_1, bytes_0]
            base_exception_0 = module_1.BaseException(*list_0)
            optional_0 = module_0.errno_from_exception(base_exception_0)
            str_2 = '0'
            str_3 = 'K'
            dict_0 = {str_1: optional_0, str_2: bytes_0, str_3: str_2, str_3: base_exception_0}
            object_dict_0 = module_0.ObjectDict(**dict_0)
            object_dict_0.__setattr__(str_0, bytes_0)
            gzip_decompressor_0 = module_0.GzipDecompressor()
            bytes_1 = gzip_decompressor_0.decompress(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
