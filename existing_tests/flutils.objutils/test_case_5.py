import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        list_0 = None
        str_0 = '\r*5W &ngxZM@p'
        list_1 = [str_0, str_0, str_0, str_0]
        bool_0 = module_0.has_attrs(list_0, *list_1)

if __name__ == "__main__":
    unittest.main()
