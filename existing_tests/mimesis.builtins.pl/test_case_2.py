import unittest
import timeout_decorator
import mimesis.builtins.pl as module_0

class Test_Pl_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.regon()
        str_1 = poland_spec_provider_0.nip()
        poland_spec_provider_1 = module_0.PolandSpecProvider()
        str_2 = poland_spec_provider_1.pesel()

if __name__ == "__main__":
    unittest.main()
