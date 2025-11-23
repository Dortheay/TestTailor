import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        tuple_0 = None
        dict_0 = {}
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
        var_0 = ansible_vault_encrypted_unicode_0.isdigit()
        bytes_0 = b'H\xb7!\xf3+@\xacq4h'
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
        var_1 = ansible_vault_encrypted_unicode_1.__radd__(tuple_0)

if __name__ == "__main__":
    unittest.main()
