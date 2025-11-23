import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xc4\x96h(\x90\xdf\x15\xd2r\xbf\xd1\xa1\xb2\xe2i/:GJ\xa0'
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
            var_0 = ansible_vault_encrypted_unicode_0.isspace()
            float_0 = 0.0
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(float_0)
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_1)
            bytes_1 = b'\x97'
            str_0 = 'ubR(H\tu\tPkTw'
            var_1 = ansible_vault_encrypted_unicode_0.count(bytes_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
