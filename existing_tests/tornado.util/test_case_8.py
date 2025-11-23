import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            timeout_error_0 = module_0.TimeoutError()
            str_0 = '0'
            gzip_decompressor_0 = module_0.GzipDecompressor()
            gzip_decompressor_1 = module_0.GzipDecompressor()
            str_1 = module_0.re_unescape(str_0)
            str_2 = '0Za$"`M8$'
            str_3 = 'DBbCZD)^b\n*JE'
            dict_0 = {str_3: str_3}
            object_dict_0 = module_0.ObjectDict(**dict_0)
            object_dict_0.__setattr__(str_3, str_3)
            any_0 = module_0.import_object(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
