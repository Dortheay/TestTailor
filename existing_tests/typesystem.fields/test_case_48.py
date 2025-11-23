import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_49(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_48(self):
        try:
            str_0 = ''
            number_0 = module_0.Number()
            str_1 = '&F'
            field_0 = module_0.Field(title=str_0, description=str_1)
            field_1 = module_0.Field()
            union_0 = field_1.__or__(field_0)
            number_1 = module_0.Number(minimum=union_0, precision=str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
