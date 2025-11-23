import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_65(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_64(self):
        try:
            array_0 = module_0.Array()
            any_0 = array_0.serialize(array_0)
            any_1 = array_0.serialize(array_0)
            int_0 = 7
            integer_0 = module_0.Integer(exclusive_maximum=int_0)
            list_0 = [int_0, integer_0]
            array_1 = module_0.Array(list_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
