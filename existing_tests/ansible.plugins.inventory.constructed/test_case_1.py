import unittest
import timeout_decorator
import ansible.plugins.inventory.constructed as module_0

class Test_Constructed_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xa0\xff\xf4\xa9\xd5lv[\xc5\x9d\x8b^:'
            inventory_module_0 = module_0.InventoryModule()
            tuple_0 = None
            dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
            var_0 = inventory_module_0.verify_file(inventory_module_0)
            inventory_module_1 = module_0.InventoryModule()
            inventory_module_2 = module_0.InventoryModule()
            var_1 = inventory_module_1.host_vars(bytes_0, tuple_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
