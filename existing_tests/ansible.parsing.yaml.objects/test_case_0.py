import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ansible_mapping_0 = module_0.AnsibleMapping()

if __name__ == "__main__":
    unittest.main()
