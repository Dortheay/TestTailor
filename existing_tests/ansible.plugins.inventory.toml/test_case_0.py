import unittest
import timeout_decorator
import ansible.plugins.inventory.toml as module_0

class Test_Toml_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 2222
            dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
            str_0 = 'collection'
            list_0 = []
            str_1 = 'p&q9C\x0c]>5Qpa'
            var_0 = module_0.convert_yaml_objects_to_native(str_1)
            list_1 = None
            var_1 = module_0.convert_yaml_objects_to_native(list_1)
            ansible_toml_encoder_0 = module_0.AnsibleTomlEncoder(*list_0)
            inventory_module_0 = module_0.InventoryModule()
            var_2 = inventory_module_0.verify_file(dict_0)
            str_2 = '"'
            dict_1 = {str_0: ansible_toml_encoder_0, str_2: int_0}
            ansible_toml_encoder_1 = module_0.AnsibleTomlEncoder(**dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
