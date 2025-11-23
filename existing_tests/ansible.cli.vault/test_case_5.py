import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b"c\xd17\xf9\tP'x \xa7\xe8\x0f\xb4"
            set_0 = {bytes_0}
            vault_c_l_i_0 = module_0.VaultCLI(set_0)
            var_0 = vault_c_l_i_0.execute_decrypt()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
