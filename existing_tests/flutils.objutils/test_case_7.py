import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'maintainer_email'
        bool_0 = module_0.is_list_like(str_0)
        list_0 = [str_0]
        bool_1 = module_0.has_any_attrs(list_0)
        list_1 = [list_0, list_0]
        list_2 = [list_0, str_0]
        tuple_0 = (str_0, list_0, list_1, list_2)
        bool_2 = module_0.is_list_like(tuple_0)
        bool_3 = module_0.has_attrs(str_0, *list_0)

if __name__ == "__main__":
    unittest.main()
