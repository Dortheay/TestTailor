import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 1636
            str_0 = None
            ansible_constructor_0 = module_0.AnsibleConstructor()
            var_0 = ansible_constructor_0.construct_yaml_seq(str_0)
            ansible_constructor_1 = module_0.AnsibleConstructor()
            var_1 = ansible_constructor_1.construct_yaml_seq(int_0)
            str_1 = 'W1wEF'
            vault_lib_0 = module_2.VaultLib()
            str_2 = 'n~PG~=DQ9@HV'
            list_0 = [str_0, int_0]
            list_1 = [var_0, str_1, list_0, ansible_constructor_0]
            bytes_0 = b'\xff8\xf7 \x0eC\xecB\x85\xddv\xac\xd5\xb1'
            mapping_node_0 = module_1.MappingNode(str_2, list_1, bytes_0)
            var_2 = ansible_constructor_0.construct_yaml_str(mapping_node_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
