import unittest
import timeout_decorator
import ansible.plugins.inventory.generator as module_0

class Test_Generator_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            str_0 = 'F}B}H'
            list_0 = [inventory_module_0, inventory_module_0]
            var_0 = inventory_module_0.verify_file(list_0)
            int_0 = 769
            list_1 = [str_0, str_0, str_0]
            bytes_0 = b'\x82Rv!b'
            float_0 = 3598.4364
            tuple_0 = (bytes_0, float_0, bytes_0, inventory_module_0)
            str_1 = ''
            inventory_module_1 = module_0.InventoryModule()
            inventory_module_2 = module_0.InventoryModule()
            var_1 = inventory_module_1.add_parents(inventory_module_0, tuple_0, str_1, list_1)
            var_2 = inventory_module_0.add_parents(inventory_module_1, int_0, inventory_module_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
