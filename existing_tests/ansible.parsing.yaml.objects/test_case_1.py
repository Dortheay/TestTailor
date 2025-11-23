import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_base_y_a_m_l_object_0)

if __name__ == "__main__":
    unittest.main()
