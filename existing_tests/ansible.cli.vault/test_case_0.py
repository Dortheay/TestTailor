import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            vault_c_l_i_0 = module_0.VaultCLI(bool_0)
            var_0 = vault_c_l_i_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
