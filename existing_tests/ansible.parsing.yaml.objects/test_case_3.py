import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'is_Identifier'
        int_0 = 70
        float_0 = -926.956
        tuple_0 = (float_0,)
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(tuple_0)
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
        var_0 = ansible_vault_encrypted_unicode_1.swapcase()
        ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(tuple_0)
        var_1 = ansible_vault_encrypted_unicode_2.isnumeric()
        ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(int_0)
        var_2 = ansible_vault_encrypted_unicode_3.__le__(str_0)
        var_3 = ansible_vault_encrypted_unicode_3.isupper()
        var_4 = ansible_vault_encrypted_unicode_3.__unicode__()

if __name__ == "__main__":
    unittest.main()
