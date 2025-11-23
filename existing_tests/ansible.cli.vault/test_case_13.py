import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'IPCoJB0=gB7PKg'
        set_0 = None
        list_0 = [str_0, set_0, str_0, str_0]
        vault_c_l_i_0 = module_0.VaultCLI(list_0)
        tuple_0 = (str_0, set_0, vault_c_l_i_0)
        set_1 = {tuple_0, str_0}
        int_0 = 2272
        vault_c_l_i_1 = module_0.VaultCLI(int_0)
        var_0 = vault_c_l_i_1.format_ciphertext_yaml(set_1)

if __name__ == "__main__":
    unittest.main()
