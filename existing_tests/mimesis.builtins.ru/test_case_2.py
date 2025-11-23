import unittest
import timeout_decorator
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

class Test_Ru_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '$EH;S}=K[oz)y4z\rE'
        russia_spec_provider_0 = module_0.RussiaSpecProvider(str_0)
        str_1 = russia_spec_provider_0.patronymic()

if __name__ == "__main__":
    unittest.main()
