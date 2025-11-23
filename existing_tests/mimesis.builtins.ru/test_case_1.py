import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.generate_sentence()

if __name__ == "__main__":
    unittest.main()
