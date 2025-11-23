import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = -350
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
            var_0 = ansible_vault_encrypted_unicode_1.__len__()
            ansible_unicode_0 = None
            var_1 = ansible_vault_encrypted_unicode_1.__mul__(ansible_unicode_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
