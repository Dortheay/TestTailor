import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        dict_0 = {}
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
        var_0 = ansible_vault_encrypted_unicode_0.isdigit()

if __name__ == "__main__":
    unittest.main()
