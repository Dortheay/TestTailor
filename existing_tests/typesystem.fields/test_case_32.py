import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        try:
            float_0 = -1589.0
            str_0 = 'e<fTPYEG^'
            number_0 = module_0.Number(minimum=float_0, maximum=float_0, precision=str_0)
            list_0 = []
            union_0 = module_0.Union(list_0)
            any_0 = union_0.validate(number_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
