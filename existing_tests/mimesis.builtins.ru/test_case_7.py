import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '.group'
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_1 = russia_spec_provider_0.inn()
        russia_spec_provider_1 = module_0.RussiaSpecProvider(str_0)
        str_2 = russia_spec_provider_1.kpp()

if __name__ == "__main__":
    unittest.main()
