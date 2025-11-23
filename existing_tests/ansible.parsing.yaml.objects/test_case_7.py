import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 708
        ansible_unicode_0 = module_0.AnsibleUnicode()
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_unicode_0)
        var_0 = ansible_vault_encrypted_unicode_0.isnumeric()
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(int_0)
        ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
        ansible_unicode_1 = module_0.AnsibleUnicode()
        var_1 = ansible_vault_encrypted_unicode_0.capitalize()
        list_0 = [ansible_unicode_1]
        ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(list_0)
        var_2 = ansible_vault_encrypted_unicode_2.rsplit()
        bool_0 = False
        ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(bool_0)

if __name__ == "__main__":
    unittest.main()
