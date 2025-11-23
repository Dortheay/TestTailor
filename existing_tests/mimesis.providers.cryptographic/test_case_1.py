import unittest
import timeout_decorator
import mimesis.providers.cryptographic as module_0

class Test_Cryptographic_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        cryptographic_0 = module_0.Cryptographic()
        int_0 = -1692
        var_0 = cryptographic_0.token_urlsafe()
        str_0 = cryptographic_0.hash()
        str_1 = cryptographic_0.hash()
        bytes_0 = cryptographic_0.token_bytes()
        var_1 = cryptographic_0.token_urlsafe()
        str_2 = cryptographic_0.mnemonic_phrase(int_0)
        str_3 = cryptographic_0.mnemonic_phrase()

if __name__ == "__main__":
    unittest.main()
