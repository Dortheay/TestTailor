import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1

class Test_Constructor_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'test_file.yaml'
        ansible_constructor_0 = module_0.AnsibleConstructor(str_0)
        str_1 = 'key'
        str_2 = 'value'
        str_3 = 'tag:yaml.org,2002:map'
        str_4 = 'tag:yaml.org,2002:str'
        mapping_node_0 = module_1.MappingNode(str_4, str_1)
        mapping_node_1 = module_1.MappingNode(str_4, str_2)
        mapping_node_2 = (mapping_node_0, mapping_node_1)
        mapping_node_3 = [mapping_node_2]
        mapping_node_4 = module_1.MappingNode(str_3, mapping_node_3)
        var_0 = ansible_constructor_0.construct_yaml_map(mapping_node_4)
        var_1 = next(var_0)

if __name__ == "__main__":
    unittest.main()
