import unittest
import timeout_decorator
import ansible.plugins.inventory.toml as module_0

class Test_Toml_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'sB'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(bytes_0)

if __name__ == "__main__":
    unittest.main()
