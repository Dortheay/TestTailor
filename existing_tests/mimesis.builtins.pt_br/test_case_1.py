import unittest
import timeout_decorator
import mimesis.builtins.pt_br as module_0

class Test_Pt_br_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        int_0 = 4
        brazil_spec_provider_0 = module_0.BrazilSpecProvider(int_0)
        str_0 = brazil_spec_provider_0.cpf(bool_0)

if __name__ == "__main__":
    unittest.main()
