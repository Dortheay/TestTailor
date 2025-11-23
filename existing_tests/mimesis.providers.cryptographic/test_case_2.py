import unittest
import timeout_decorator
import mimesis.providers.cryptographic as module_0

class Test_Cryptographic_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = None
        cryptographic_0 = module_0.Cryptographic()
        str_0 = cryptographic_0.token_hex(int_0)

if __name__ == "__main__":
    unittest.main()
