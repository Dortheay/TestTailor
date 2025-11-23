import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_62(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_61(self):
        try:
            str_0 = '0r%9Bg+\\YH2z(8['
            str_1 = '\\'
            str_2 = "9sci9RhPs'p}GW\rum\x0cvm"
            dict_0 = {str_0: str_0, str_1: str_1, str_2: str_2}
            tuple_0 = (dict_0,)
            object_0 = module_0.Object(additional_properties=tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
