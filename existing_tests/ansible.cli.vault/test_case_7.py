import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            float_0 = 1845.1745
            vault_c_l_i_0 = module_0.VaultCLI(float_0)
            var_0 = vault_c_l_i_0.execute_edit()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
