import unittest
import timeout_decorator
import mimesis.builtins.pt_br as module_0

class Test_Pt_br_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        brazil_spec_provider_0 = module_0.BrazilSpecProvider()
        str_0 = 'whAx/u{gnnEr }KBR'
        str_1 = brazil_spec_provider_0.cpf()
        brazil_spec_provider_1 = module_0.BrazilSpecProvider(str_0)

if __name__ == "__main__":
    unittest.main()
