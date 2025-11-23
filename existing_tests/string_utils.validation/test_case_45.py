import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_35(self):
        str_0 = '9780312498580'
        bool_0 = module_0.is_isbn(str_0)
        str_1 = '1506715214'
        bool_1 = module_0.is_isbn(str_1)
        str_2 = '978-0312498580'
        bool_2 = module_0.is_isbn(str_2)
        str_3 = '150-6715214'
        bool_3 = module_0.is_isbn(str_3)
        bool_4 = False
        bool_5 = module_0.is_isbn(str_3, bool_4)
        bool_6 = module_0.is_isbn(str_2, bool_4)
        str_4 = '123456789'
        bool_7 = module_0.is_isbn(str_4)
        str_5 = ''
        bool_8 = module_0.is_isbn(str_5)
        bool_9 = module_0.is_ip(str_5)
        var_0 = None
        bool_10 = module_0.is_ip(var_0)

if __name__ == "__main__":
    unittest.main()
