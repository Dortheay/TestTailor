import unittest
import timeout_decorator
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.vault as module_2

class Test_Constructor_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = None
            bytes_0 = b'6\xfa\xc7\x9e\xf7\x83\xa1\xe5\xea"h*]\xf3|N\x88\x0f'
            dict_1 = {bytes_0: bytes_0, bytes_0: bytes_0}
            float_0 = 0.2
            ansible_constructor_0 = module_0.AnsibleConstructor(dict_1, float_0)
            var_0 = ansible_constructor_0.construct_vault_encrypted_unicode(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
