import unittest
import timeout_decorator
import httpie.cli.definition as module_0

class Test_Definition_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            auth_type_lazy_choices_0 = module_0._AuthTypeLazyChoices()
            auth_type_lazy_choices_1 = module_0._AuthTypeLazyChoices()
            var_0 = auth_type_lazy_choices_0.__iter__()
            auth_type_lazy_choices_2 = module_0._AuthTypeLazyChoices()
            str_0 = 'c'
            var_1 = auth_type_lazy_choices_0.__iter__()
            dict_0 = {}
            auth_type_lazy_choices_3 = module_0._AuthTypeLazyChoices(**dict_0)
            var_2 = auth_type_lazy_choices_3.__iter__()
            dict_1 = {str_0: str_0}
            str_1 = None
            str_2 = 'I\r'
            float_0 = 0.1
            dict_2 = {str_1: dict_1, str_1: auth_type_lazy_choices_0, str_2: float_0}
            str_3 = '--verbose'
            var_3 = auth_type_lazy_choices_3.__contains__(str_3)
            var_4 = auth_type_lazy_choices_3.__iter__()
            auth_type_lazy_choices_4 = module_0._AuthTypeLazyChoices(**dict_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
