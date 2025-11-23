import unittest
import timeout_decorator
import ansible.plugins.inventory.toml as module_0

class Test_Toml_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'XUK9CbWtt&\x0cxs//'
            list_0 = [str_0, str_0]
            ansible_toml_encoder_0 = module_0.AnsibleTomlEncoder()
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.verify_file(ansible_toml_encoder_0)
            str_1 = 'CAa1q\x0bWf*]#xLY['
            inventory_module_1 = module_0.InventoryModule()
            str_2 = '\x0cos)7J\\'
            bool_0 = False
            str_3 = 't9+:Gj<^Sr{'
            dict_0 = {str_2: str_1, str_2: bool_0, str_3: str_3}
            var_1 = module_0.convert_yaml_objects_to_native(dict_0)
            var_2 = inventory_module_0.parse(str_0, ansible_toml_encoder_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
