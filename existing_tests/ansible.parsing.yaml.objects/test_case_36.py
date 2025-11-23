import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            ansible_mapping_0 = module_0.AnsibleMapping()
            list_0 = [ansible_mapping_0, ansible_mapping_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_0 = ansible_vault_encrypted_unicode_0.__hash__()
            ansible_unicode_0 = None
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_unicode_0)
            int_0 = 999999999999
            var_1 = ansible_vault_encrypted_unicode_1.__getitem__(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
