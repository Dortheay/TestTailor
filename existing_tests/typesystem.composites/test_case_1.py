import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'if'
            field_0 = module_1.Field()
            list_0 = [field_0, field_0, field_0, field_0]
            one_of_0 = module_0.OneOf(list_0)
            any_0 = one_of_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
