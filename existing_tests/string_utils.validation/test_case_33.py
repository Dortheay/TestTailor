import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        bytes_0 = b"\xef<\x81\x15\xab.\x8f\xc9\xf6.S'O\xe2"
        str_0 = '^([a-z]+\\d*_[a-z\\d_]*|_+[a-z\\d]+[a-z\\d_]*)$'
        bool_0 = module_0.is_isbn_10(str_0)
        none_type_0 = None
        str_1 = 'pBLl1q)-]MLCkbM4Mgj'
        bool_1 = module_0.is_pangram(bytes_0)
        bool_2 = module_0.is_number(str_1)
        bool_3 = False
        bool_4 = module_0.is_isbn_13(str_1, bool_3)
        bool_5 = module_0.is_full_string(bool_2)
        bool_6 = module_0.is_url(bytes_0, none_type_0)

if __name__ == "__main__":
    unittest.main()
