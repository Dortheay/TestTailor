import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_35(self):
        try:
            str_0 = 'This field is required.'
            field_0 = module_0.Field(title=str_0, default=str_0)
            str_1 = 'm8dgt'
            str_2 = None
            dict_0 = {str_1: str_1, str_2: str_1}
            choice_0 = module_0.Choice(choices=dict_0)
            any_0 = choice_0.validate(field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
