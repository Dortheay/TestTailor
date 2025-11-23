import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '/'
        import_from_0 = module_1.ImportFrom()
        str_1 = 'i q'
        int_0 = 1
        int_1 = 8271
        dict_0 = {str_1: int_0, str_0: int_1, str_1: int_1}
        str_2 = 'T<xa'
        str_3 = '%}/>*~gEZn\x0bz<.51,'
        str_4 = '3mb^6zX1'
        dict_1 = {str_2: str_3, str_3: str_3, str_3: str_2, str_4: str_2}
        parser_0 = module_0.Parser(dict_0, dict_1)
        parser_0.imports(str_0, import_from_0)
        bool_0 = module_0.is_public_family(str_0)

if __name__ == "__main__":
    unittest.main()
