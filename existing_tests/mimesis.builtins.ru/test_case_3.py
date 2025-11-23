import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.passport_series()
        russia_spec_provider_1 = module_0.RussiaSpecProvider()
        int_0 = russia_spec_provider_1.passport_number()

if __name__ == "__main__":
    unittest.main()
