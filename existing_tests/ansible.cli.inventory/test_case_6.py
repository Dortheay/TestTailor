import unittest
import timeout_decorator
import ansible.cli.inventory as module_0

class Test_Inventory_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '$:7D2%+ORABkK'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            inventory_c_l_i_0 = module_0.InventoryCLI(dict_0)
            var_0 = inventory_c_l_i_0.toml_inventory(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
