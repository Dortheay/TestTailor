import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_66(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_41(self):
        try:
            bytes_0 = b'encrypted_data'
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
            var_0 = ansible_vault_encrypted_unicode_0.is_encrypted()
            var_1 = ansible_vault_encrypted_unicode_0.translate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
