import unittest
import timeout_decorator
import ansible.cli.vault as module_0

class Test_Vault_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            float_0 = 3337.378
            int_0 = 2798
            list_0 = [float_0]
            vault_c_l_i_0 = module_0.VaultCLI(list_0)
            tuple_0 = None
            dict_0 = {int_0: float_0, int_0: int_0, vault_c_l_i_0: tuple_0}
            vault_c_l_i_1 = module_0.VaultCLI(dict_0)
            var_0 = vault_c_l_i_1.execute_create()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
