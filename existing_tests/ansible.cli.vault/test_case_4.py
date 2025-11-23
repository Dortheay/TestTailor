import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'V<C4:&&F,'
            vault_c_l_i_0 = module_0.VaultCLI(str_0)
            var_0 = vault_c_l_i_0.execute_encrypt_string()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
