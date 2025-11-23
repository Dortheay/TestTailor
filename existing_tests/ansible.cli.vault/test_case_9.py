import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'Error creating AnsibleVaultEncryptedUnicode, invalid vault (%s) provided'
            vault_c_l_i_0 = module_0.VaultCLI(str_0)
            var_0 = vault_c_l_i_0.execute_rekey()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
