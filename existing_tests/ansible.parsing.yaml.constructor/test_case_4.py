import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = None
            list_0 = [float_0]
            str_0 = 'OO{P2lf)vs~py1'
            str_1 = 'qO$pOz!p'
            mapping_node_0 = module_1.MappingNode(list_0, str_0, str_1, list_0)
            ansible_constructor_0 = module_0.AnsibleConstructor(str_0, str_0)
            var_0 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
