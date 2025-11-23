import unittest
import timeout_decorator
import mimesis.builtins.pl as module_0

class Test_Pl_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.pesel()
        str_1 = poland_spec_provider_0.regon()

if __name__ == "__main__":
    unittest.main()
