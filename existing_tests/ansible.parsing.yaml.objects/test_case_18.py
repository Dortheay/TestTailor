import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        set_0 = set()
        float_0 = -944.0
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(float_0)
        var_0 = ansible_vault_encrypted_unicode_0.__eq__(set_0)

if __name__ == "__main__":
    unittest.main()
