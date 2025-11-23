import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.snils()

if __name__ == "__main__":
    unittest.main()
