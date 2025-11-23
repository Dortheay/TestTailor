import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = -1829
        vault_c_l_i_0 = module_0.VaultCLI(int_0)

if __name__ == "__main__":
    unittest.main()
