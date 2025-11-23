import unittest
import timeout_decorator
import ansible.cli.inventory as module_0

class Test_Inventory_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '_'
            inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
            var_0 = inventory_c_l_i_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
