import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        ansible_mapping_0 = module_0.AnsibleMapping()
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
        var_0 = ansible_vault_encrypted_unicode_0.isascii()

if __name__ == "__main__":
    unittest.main()
