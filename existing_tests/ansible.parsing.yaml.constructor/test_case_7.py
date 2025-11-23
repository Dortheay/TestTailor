import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'test_file.yml'
            var_0 = None
            ansible_constructor_0 = module_0.AnsibleConstructor(str_0, var_0)
            str_1 = 'tag:yaml.org,2002:map'
            str_2 = 'tag:yaml.org,2002:str'
            str_3 = 'key1'
            mapping_node_0 = module_1.MappingNode(str_2, str_3)
            str_4 = 'value1'
            mapping_node_1 = module_1.MappingNode(str_2, str_4)
            mapping_node_2 = (mapping_node_0, mapping_node_1)
            str_5 = 'key2'
            mapping_node_3 = module_1.MappingNode(str_2, str_5)
            str_6 = 'value2'
            mapping_node_4 = module_1.MappingNode(str_2, str_6)
            mapping_node_5 = (mapping_node_3, mapping_node_4)
            mapping_node_6 = [mapping_node_2, mapping_node_5]
            mapping_node_7 = module_1.MappingNode(str_1, mapping_node_6)
            var_1 = ansible_constructor_0.construct_yaml_map(mapping_node_7)
            var_2 = next(var_1)
            var_3 = None
            var_4 = next(var_1, var_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
