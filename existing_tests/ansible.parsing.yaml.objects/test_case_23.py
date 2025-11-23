import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        str_0 = 'encrypted_data1'
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
        str_1 = 'encrypted_data2'
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(str_1)
        var_0 = ansible_vault_encrypted_unicode_0.__ge__(ansible_vault_encrypted_unicode_1)
        str_2 = 'another_plaintext'
        var_1 = ansible_vault_encrypted_unicode_0.__ge__(str_2)
        str_3 = 'z_plaintext'
        var_2 = ansible_vault_encrypted_unicode_0.__ge__(str_3)
        str_4 = 'no_vault_data'
        ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(str_4)
        str_5 = 'any_plaintext'
        var_3 = ansible_vault_encrypted_unicode_2.__ge__(str_5)

if __name__ == "__main__":
    unittest.main()
