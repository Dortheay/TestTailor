import unittest
import timeout_decorator
import mimesis.builtins.pt_br as module_0

class Test_Pt_br_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bool_0 = False
        brazil_spec_provider_0 = module_0.BrazilSpecProvider()
        str_0 = brazil_spec_provider_0.cpf(bool_0)
        str_1 = brazil_spec_provider_0.cnpj()
        str_2 = brazil_spec_provider_0.cpf()
        bool_1 = False
        str_3 = brazil_spec_provider_0.cnpj(bool_1)
        str_4 = brazil_spec_provider_0.cnpj()

if __name__ == "__main__":
    unittest.main()
