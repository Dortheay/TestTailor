import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.kpp()
        str_1 = russia_spec_provider_0.series_and_number()
        str_2 = russia_spec_provider_0.ogrn()
        int_0 = russia_spec_provider_0.passport_number()
        str_3 = russia_spec_provider_0.snils()
        str_4 = russia_spec_provider_0.ogrn()
        int_1 = russia_spec_provider_0.passport_number()
        int_2 = russia_spec_provider_0.passport_number()

if __name__ == "__main__":
    unittest.main()
