import unittest
import timeout_decorator
import mimesis.providers.cryptographic as module_0

class Test_Cryptographic_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = 1989
        str_0 = 'J KF$6\x0chHvZ]P='
        cryptographic_0 = module_0.Cryptographic()
        str_1 = cryptographic_0.mnemonic_phrase(int_0, str_0)

if __name__ == "__main__":
    unittest.main()
