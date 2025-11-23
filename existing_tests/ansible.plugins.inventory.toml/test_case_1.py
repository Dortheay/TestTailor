import unittest
import timeout_decorator
import ansible.plugins.inventory.toml as module_0

class Test_Toml_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            list_0 = [inventory_module_0]
            ansible_toml_encoder_0 = module_0.AnsibleTomlEncoder()
            var_0 = inventory_module_0.parse(list_0, list_0, inventory_module_0, ansible_toml_encoder_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
