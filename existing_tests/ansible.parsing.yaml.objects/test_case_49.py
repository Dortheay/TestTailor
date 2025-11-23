import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_50(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        try:
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
            dict_0 = {}
            ansible_mapping_0 = module_0.AnsibleMapping(**dict_0)
            str_0 = 'CQRkKny7fD'
            ansible_unicode_0 = module_0.AnsibleUnicode(**dict_0)
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_unicode_0)
            var_0 = ansible_vault_encrypted_unicode_0.rpartition(str_0)
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
            var_1 = ansible_vault_encrypted_unicode_1.isspace()
            var_2 = ansible_vault_encrypted_unicode_1.__int__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
