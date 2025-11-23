import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        bytes_0 = b'i\xdf\xb1\x1b(\x0c>\xb51P\x84h\x15\xcd0\xd2\xea\x88'
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
        var_0 = ansible_vault_encrypted_unicode_0.isspace()

if __name__ == "__main__":
    unittest.main()
