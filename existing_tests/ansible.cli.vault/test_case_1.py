import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '16W'
            str_1 = 'F)]}S7'
            vault_c_l_i_0 = module_0.VaultCLI(str_1)
            vault_c_l_i_1 = module_0.VaultCLI(str_0)
            var_0 = vault_c_l_i_1.init_parser()
            var_1 = vault_c_l_i_1.execute_encrypt_string()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
