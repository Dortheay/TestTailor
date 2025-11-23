import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = False
        str_0 = 'tj/=!oV;*6;'
        list_0 = [str_0, str_0, str_0, str_0]
        bool_1 = module_0.has_any_attrs(bool_0, *list_0)

if __name__ == "__main__":
    unittest.main()
