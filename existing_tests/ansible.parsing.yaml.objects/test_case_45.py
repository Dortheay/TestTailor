import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            dict_0 = None
            float_0 = 379.25
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(float_0)
            var_0 = ansible_vault_encrypted_unicode_0.__str__()
            var_1 = ansible_vault_encrypted_unicode_0.join(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
