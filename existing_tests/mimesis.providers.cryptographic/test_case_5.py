import unittest
import timeout_decorator
import mimesis.providers.cryptographic as module_0

class Test_Cryptographic_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        cryptographic_0 = module_0.Cryptographic()
        var_0 = cryptographic_0.uuid()
        int_0 = 995
        bool_0 = False
        str_0 = cryptographic_0.mnemonic_phrase(int_0, bool_0)

if __name__ == "__main__":
    unittest.main()
