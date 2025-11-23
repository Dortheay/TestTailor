import unittest
import timeout_decorator
import mimesis.providers.cryptographic as module_0

class Test_Cryptographic_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            cryptographic_0 = module_0.Cryptographic()
            cryptographic_1 = module_0.Cryptographic(**dict_0)
            cryptographic_2 = module_0.Cryptographic()
            str_0 = cryptographic_2.mnemonic_phrase()
            str_1 = cryptographic_1.hash()
            bool_0 = True
            var_0 = cryptographic_0.uuid(bool_0)
            str_2 = cryptographic_1.hash()
            int_0 = -92
            str_3 = cryptographic_1.token_hex(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
