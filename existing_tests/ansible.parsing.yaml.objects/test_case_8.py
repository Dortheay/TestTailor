import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        dict_0 = {}
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
        var_0 = ansible_vault_encrypted_unicode_0.__str__()
        str_0 = ' ode'
        set_0 = {str_0, str_0, str_0}
        dict_1 = {str_0: set_0, str_0: str_0, str_0: str_0}
        list_0 = [var_0, var_0]
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_0)
        var_1 = ansible_vault_encrypted_unicode_1.isalnum()
        var_2 = ansible_vault_encrypted_unicode_0.__radd__(set_0)
        list_1 = [dict_1, set_0, var_2]
        var_3 = ansible_vault_encrypted_unicode_1.__eq__(list_1)
        var_4 = ansible_vault_encrypted_unicode_0.is_encrypted()
        ansible_mapping_0 = module_0.AnsibleMapping(**dict_1)

if __name__ == "__main__":
    unittest.main()
