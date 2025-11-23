import unittest
import timeout_decorator
import mimesis.providers.cryptographic as module_0

class Test_Cryptographic_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        cryptographic_0 = module_0.Cryptographic()
        str_0 = cryptographic_0.token_hex()
        cryptographic_1 = module_0.Cryptographic()
        var_0 = cryptographic_1.token_urlsafe()
        str_1 = cryptographic_1.hash()
        str_2 = cryptographic_1.token_hex()

if __name__ == "__main__":
    unittest.main()
