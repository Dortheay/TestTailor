import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1

class Test_Constructor_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ansible_constructor_0 = module_0.AnsibleConstructor()

if __name__ == "__main__":
    unittest.main()
