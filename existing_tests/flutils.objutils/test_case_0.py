import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = []
            str_0 = '__name__'
            str_1 = 'X/4o(zp5p29Q\r~t7'
            bool_0 = module_0.has_any_callables(str_0)
            str_2 = 'index'
            list_1 = [str_1, str_2, str_2]
            bool_1 = module_0.has_attrs(list_0, *list_1)
            bool_2 = module_0.has_callables(bool_1)
            list_2 = [str_0, str_1, str_2, str_2]
            bool_3 = module_0.has_any_callables(list_1)
            bool_4 = module_0.has_any_callables(list_0, *list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
