import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -3002
            vault_c_l_i_0 = module_0.VaultCLI(int_0)
            dict_0 = {}
            var_0 = vault_c_l_i_0.post_process_args(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
