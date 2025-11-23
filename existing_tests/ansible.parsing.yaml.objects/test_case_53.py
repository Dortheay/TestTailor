import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_54(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            set_0 = set()
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(set_0)
            var_0 = ansible_vault_encrypted_unicode_0.__unicode__()
            bytes_0 = b'a\xc5\x99`\xca\xbdd\x05\xden\xfc\x06j\x8e\x0e\xab\x04'
            var_1 = ansible_vault_encrypted_unicode_0.startswith(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
