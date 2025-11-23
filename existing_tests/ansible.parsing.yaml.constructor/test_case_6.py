import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            list_0 = []
            int_0 = 23
            mapping_node_0 = module_1.MappingNode(int_0, list_0)
            str_0 = 'Y'
            dict_0 = {}
            str_1 = 'X?$Vk\x0cZ_0'
            vault_lib_0 = module_2.VaultLib(str_1)
            float_0 = 0.0001
            tuple_0 = (dict_0, vault_lib_0, float_0, str_0)
            ansible_constructor_0 = module_0.AnsibleConstructor(tuple_0)
            var_0 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
