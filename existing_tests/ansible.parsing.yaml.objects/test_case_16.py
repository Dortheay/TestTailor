import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        str_0 = 'h%6%l'
        ansible_unicode_0 = module_0.AnsibleUnicode()
        int_0 = 4095
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
        var_0 = ansible_vault_encrypted_unicode_0.format_map(str_0)

if __name__ == "__main__":
    unittest.main()
