import unittest
import timeout_decorator
import ansible.parsing.yaml.loader as module_0

class Test_Loader_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'U\x03\xd9\xd2-\xb0\xfb\x86\x84\x98q\xd0\x8e\xf5\x8b\xf4\xc5)'
        ansible_loader_0 = module_0.AnsibleLoader(bytes_0)

if __name__ == "__main__":
    unittest.main()
