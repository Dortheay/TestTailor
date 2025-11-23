import unittest
import timeout_decorator
import ansible.cli.inventory as module_0

class Test_Inventory_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 1519
            bool_0 = True
            inventory_c_l_i_0 = module_0.InventoryCLI(bool_0)
            var_0 = inventory_c_l_i_0.json_inventory(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
