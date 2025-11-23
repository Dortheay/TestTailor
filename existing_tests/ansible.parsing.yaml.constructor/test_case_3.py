import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            ansible_constructor_0 = module_0.AnsibleConstructor()
            bool_0 = False
            var_0 = ansible_constructor_0.construct_yaml_unsafe(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
