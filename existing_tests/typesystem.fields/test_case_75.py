import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_76(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_75(self):
        try:
            date_0 = module_0.Date()
            float_0 = -1859.7676706997895
            number_0 = module_0.Number(minimum=float_0, multiple_of=float_0)
            const_0 = module_0.Const(number_0)
            int_0 = 3616
            list_0 = []
            tuple_0 = (int_0, list_0)
            object_0 = module_0.Object(properties=const_0, required=tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
