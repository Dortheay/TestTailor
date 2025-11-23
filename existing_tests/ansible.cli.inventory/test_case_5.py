import unittest
import timeout_decorator
import ansible.cli.inventory as module_0

class Test_Inventory_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = True
            dict_0 = None
            bool_1 = False
            dict_1 = {dict_0: bool_1}
            inventory_c_l_i_0 = module_0.InventoryCLI(dict_1)
            inventory_c_l_i_1 = module_0.InventoryCLI(inventory_c_l_i_0)
            set_0 = {inventory_c_l_i_1, bool_1, dict_0}
            inventory_c_l_i_2 = module_0.InventoryCLI(set_0)
            var_0 = inventory_c_l_i_2.yaml_inventory(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
