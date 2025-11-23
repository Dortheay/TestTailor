import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.generate_sentence()
        str_1 = russia_spec_provider_0.series_and_number()
        str_2 = russia_spec_provider_0.snils()
        russia_spec_provider_1 = module_0.RussiaSpecProvider()
        str_3 = russia_spec_provider_1.patronymic()
        russia_spec_provider_2 = module_0.RussiaSpecProvider()
        int_0 = russia_spec_provider_2.passport_number()
        russia_spec_provider_3 = module_0.RussiaSpecProvider()
        str_4 = russia_spec_provider_3.series_and_number()
        str_5 = russia_spec_provider_3.inn()
        str_6 = russia_spec_provider_0.patronymic()
        str_7 = russia_spec_provider_0.passport_series()
        str_8 = russia_spec_provider_3.generate_sentence()
        str_9 = russia_spec_provider_2.kpp()
        str_10 = russia_spec_provider_2.series_and_number()
        str_11 = russia_spec_provider_2.bic()
        str_12 = russia_spec_provider_2.bic()
        str_13 = russia_spec_provider_2.generate_sentence()
        bytes_0 = b'\x7f\x7f\xa9\xefsW\xe88'
        russia_spec_provider_4 = module_0.RussiaSpecProvider(bytes_0)
        str_14 = russia_spec_provider_4.kpp()
        str_15 = russia_spec_provider_4.snils()
        str_16 = russia_spec_provider_3.kpp()
        russia_spec_provider_5 = module_0.RussiaSpecProvider(bytes_0)
        str_17 = russia_spec_provider_5.series_and_number()
        str_18 = russia_spec_provider_2.kpp()
        str_19 = russia_spec_provider_2.generate_sentence()
        str_20 = russia_spec_provider_5.patronymic()
        str_21 = russia_spec_provider_3.bic()
        str_22 = russia_spec_provider_3.generate_sentence()

if __name__ == "__main__":
    unittest.main()
