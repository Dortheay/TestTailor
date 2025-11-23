import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.kpp()
        int_0 = -638
        russia_spec_provider_1 = module_0.RussiaSpecProvider(int_0)
        str_1 = russia_spec_provider_1.series_and_number()
        russia_spec_provider_2 = module_0.RussiaSpecProvider()
        str_2 = russia_spec_provider_2.passport_series()
        str_3 = russia_spec_provider_2.bic()

if __name__ == "__main__":
    unittest.main()
