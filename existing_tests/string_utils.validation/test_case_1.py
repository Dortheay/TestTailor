import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'PP1'
            bool_0 = module_0.is_camel_case(str_0)
            str_1 = '?b..KHny^TpaMS.I=99'
            bytes_0 = b'\x85r\x83\xbb\x87\xfc\x9bj\x17\xc6'
            float_0 = 2857.7
            tuple_0 = (str_0, str_1, bytes_0, float_0)
            optional_0 = None
            bool_1 = module_0.is_url(tuple_0, optional_0)
            str_2 = None
            bool_2 = module_0.is_decimal(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
