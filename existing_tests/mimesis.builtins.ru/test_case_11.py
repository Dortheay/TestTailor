import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        russia_spec_provider_1 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.series_and_number()
        str_1 = russia_spec_provider_0.bic()
        str_2 = russia_spec_provider_1.inn()
        russia_spec_provider_2 = module_0.RussiaSpecProvider()
        str_3 = russia_spec_provider_2.ogrn()
        str_4 = russia_spec_provider_2.generate_sentence()
        str_5 = russia_spec_provider_2.snils()
        str_6 = russia_spec_provider_2.snils()
        str_7 = russia_spec_provider_2.snils()
        int_0 = russia_spec_provider_0.passport_number()
        str_8 = russia_spec_provider_2.bic()
        str_9 = russia_spec_provider_2.series_and_number()
        str_10 = russia_spec_provider_2.bic()
        russia_spec_provider_3 = module_0.RussiaSpecProvider()
        str_11 = russia_spec_provider_0.ogrn()
        str_12 = russia_spec_provider_0.bic()
        russia_spec_provider_4 = module_0.RussiaSpecProvider()
        str_13 = russia_spec_provider_0.bic()
        int_1 = russia_spec_provider_4.passport_number()
        str_14 = russia_spec_provider_1.snils()

if __name__ == "__main__":
    unittest.main()
