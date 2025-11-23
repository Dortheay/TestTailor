import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'encrypted_value'
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
        int_0 = 5
        int_1 = 15
        var_0 = ansible_vault_encrypted_unicode_0.__getslice__(int_0, int_1)

if __name__ == "__main__":
    unittest.main()
