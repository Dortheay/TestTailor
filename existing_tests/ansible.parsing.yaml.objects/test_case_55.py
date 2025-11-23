import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_56(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            ansible_unicode_0 = module_0.AnsibleUnicode()
            float_0 = -1104.0
            int_0 = -881
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            var_0 = ansible_vault_encrypted_unicode_0.zfill(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
