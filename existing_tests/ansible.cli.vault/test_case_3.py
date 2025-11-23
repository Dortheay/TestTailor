import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 0.5
            vault_c_l_i_0 = module_0.VaultCLI(float_0)
            bytes_0 = b'\xb6\xbb\xc1\xc8\x11+E\xac\x98\xae<5C|u\x059\xeb\xcf'
            bytes_1 = b'\x196\xe0T\xc7\x83\x94\xaeA\x1f\xa2\x9as\xc50\xea\x02\xdd'
            var_0 = vault_c_l_i_0.format_ciphertext_yaml(vault_c_l_i_0, bytes_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
