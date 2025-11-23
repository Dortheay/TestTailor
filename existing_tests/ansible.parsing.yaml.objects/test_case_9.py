import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_base_y_a_m_l_object_0)
        var_0 = ansible_vault_encrypted_unicode_0.isdecimal()

if __name__ == "__main__":
    unittest.main()
