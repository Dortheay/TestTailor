import unittest
import timeout_decorator
import ansible.plugins.inventory.ini as module_0

class Test_Ini_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            int_0 = -777
            tuple_0 = None
            var_0 = inventory_module_0.parse(int_0, tuple_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
