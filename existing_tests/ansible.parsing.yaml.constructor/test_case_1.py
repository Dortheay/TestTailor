import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -3552.767324
            dict_0 = {float_0: float_0}
            ansible_constructor_0 = module_0.AnsibleConstructor()
            var_0 = ansible_constructor_0.construct_yaml_str(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
