import unittest
import timeout_decorator
import mimesis.builtins.pl as module_0

class Test_Pl_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = 'application/vnd.ezpix-package'
        str_1 = poland_spec_provider_0.nip()
        str_2 = poland_spec_provider_0.regon()
        poland_spec_provider_1 = module_0.PolandSpecProvider()
        str_3 = poland_spec_provider_1.nip()
        poland_spec_provider_2 = module_0.PolandSpecProvider(str_0)
        str_4 = poland_spec_provider_2.nip()
        poland_spec_provider_3 = module_0.PolandSpecProvider()
        str_5 = poland_spec_provider_2.pesel()
        poland_spec_provider_4 = module_0.PolandSpecProvider()
        str_6 = poland_spec_provider_3.pesel()

if __name__ == "__main__":
    unittest.main()
