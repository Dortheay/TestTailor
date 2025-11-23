import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_69(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_44(self):
        try:
            str_0 = 'abcdef'
            var_0 = module_1.to_bytes(str_0)
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(var_0)
            int_0 = 0
            int_1 = 3
            var_1 = ansible_vault_encrypted_unicode_0.__getslice__(int_0, int_1)
            int_2 = 1
            int_3 = 5
            var_2 = ansible_vault_encrypted_unicode_0.__getslice__(int_2, int_3)
            var_3 = ansible_vault_encrypted_unicode_0.__getslice__(int_0, int_0)
            list_0 = []
            ansible_mapping_0 = module_0.AnsibleMapping(*list_0)
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
            var_4 = ansible_vault_encrypted_unicode_1.__reversed__()
            var_5 = ansible_vault_encrypted_unicode_0.rfind(ansible_vault_encrypted_unicode_0)
            str_1 = ''
            var_6 = module_1.to_bytes(int_3, str_1, ansible_vault_encrypted_unicode_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
