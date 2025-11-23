import unittest
import timeout_decorator
import mimesis.providers.cryptographic as module_0

class Test_Cryptographic_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        cryptographic_0 = module_0.Cryptographic()
        str_0 = cryptographic_0.hash()

if __name__ == "__main__":
    unittest.main()
