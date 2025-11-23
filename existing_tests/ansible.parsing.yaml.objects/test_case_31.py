import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            ansible_unicode_0 = None
            bool_0 = True
            ansible_mapping_0 = module_0.AnsibleMapping()
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
            var_0 = ansible_vault_encrypted_unicode_0.__hash__()
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(bool_0)
            var_1 = ansible_vault_encrypted_unicode_1.find(ansible_unicode_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
