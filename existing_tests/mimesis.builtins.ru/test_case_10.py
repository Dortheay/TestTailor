import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.ogrn()
        str_1 = russia_spec_provider_0.generate_sentence()
        str_2 = russia_spec_provider_0.snils()
        int_0 = -1922
        str_3 = russia_spec_provider_0.passport_series(int_0)
        russia_spec_provider_1 = module_0.RussiaSpecProvider(str_2)
        str_4 = russia_spec_provider_1.snils()
        russia_spec_provider_2 = module_0.RussiaSpecProvider(str_2)
        str_5 = russia_spec_provider_0.bic()
        int_1 = russia_spec_provider_2.passport_number()
        str_6 = russia_spec_provider_0.series_and_number()
        str_7 = russia_spec_provider_1.patronymic()

if __name__ == "__main__":
    unittest.main()
