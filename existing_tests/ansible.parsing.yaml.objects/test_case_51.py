import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_52(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            bool_0 = True
            int_0 = 1481
            list_0 = [int_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_0 = ansible_vault_encrypted_unicode_0.__rmod__(bool_0)
            int_1 = None
            ansible_mapping_0 = module_0.AnsibleMapping()
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
            var_1 = ansible_vault_encrypted_unicode_1.isspace()
            var_2 = ansible_vault_encrypted_unicode_1.rsplit()
            float_0 = -503.3
            set_0 = {ansible_vault_encrypted_unicode_1, int_1, float_0, var_1}
            var_3 = ansible_vault_encrypted_unicode_1.__ge__(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
