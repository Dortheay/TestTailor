import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.patronymic()
        int_0 = russia_spec_provider_0.passport_number()
        str_1 = russia_spec_provider_0.bic()
        str_2 = russia_spec_provider_0.patronymic()
        str_3 = russia_spec_provider_0.snils()
        str_4 = russia_spec_provider_0.kpp()
        str_5 = russia_spec_provider_0.kpp()
        russia_spec_provider_1 = module_0.RussiaSpecProvider(str_4)
        str_6 = russia_spec_provider_1.generate_sentence()
        str_7 = russia_spec_provider_0.snils()
        russia_spec_provider_2 = module_0.RussiaSpecProvider()
        gender_0 = module_1.Gender.FEMALE
        str_8 = russia_spec_provider_0.patronymic(gender_0)
        str_9 = russia_spec_provider_2.inn()
        russia_spec_provider_3 = module_0.RussiaSpecProvider()
        str_10 = russia_spec_provider_0.bic()
        str_11 = russia_spec_provider_0.ogrn()
        str_12 = russia_spec_provider_0.passport_series()
        str_13 = russia_spec_provider_2.bic()
        str_14 = russia_spec_provider_3.generate_sentence()
        str_15 = russia_spec_provider_2.snils()

if __name__ == "__main__":
    unittest.main()
