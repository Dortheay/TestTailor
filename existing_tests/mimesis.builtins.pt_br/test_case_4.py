import unittest
import timeout_decorator
import mimesis.builtins.pt_br as module_0

class Test_Pt_br_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        brazil_spec_provider_0 = module_0.BrazilSpecProvider()
        str_0 = brazil_spec_provider_0.cnpj()

if __name__ == "__main__":
    unittest.main()
