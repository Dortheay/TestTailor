import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'T'
            str_1 = None
            list_0 = []
            str_2 = '^[a-f\\d]{8}-[a-f\\d]{4}-[a-f\\d]{4}-[a-f\\d]{4}-[a-f\\d]{12}$'
            dict_0 = {str_0: list_0, str_0: str_0, str_1: str_2, str_2: str_0}
            bool_0 = module_0.is_snake_case(dict_0)
            bool_1 = True
            bool_2 = module_0.is_isbn_10(str_1, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
