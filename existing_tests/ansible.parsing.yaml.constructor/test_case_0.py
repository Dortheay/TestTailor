import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xcd\xf1x6\x1c\xcf\x8f\xcfS\xcf\x14j\xdd\xdf\x0f\xd7'
            ansible_constructor_0 = module_0.AnsibleConstructor()
            var_0 = ansible_constructor_0.construct_mapping(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
