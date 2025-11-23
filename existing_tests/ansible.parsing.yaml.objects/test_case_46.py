import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_47(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            float_0 = 41.03328
            set_0 = None
            int_0 = 70
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            var_0 = ansible_vault_encrypted_unicode_0.replace(float_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
