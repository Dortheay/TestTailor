import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 30
            bool_0 = True
            str_0 = 'wD'
            dict_0 = {str_0: str_0, bool_0: bool_0}
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
            tuple_0 = (bool_0, str_0, ansible_vault_encrypted_unicode_0, ansible_base_y_a_m_l_object_0)
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(tuple_0)
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_1)
            ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_2)
            var_0 = ansible_vault_encrypted_unicode_3.center(int_0)
            float_0 = 0.0001
            ansible_vault_encrypted_unicode_4 = module_0.AnsibleVaultEncryptedUnicode(float_0)
            var_1 = ansible_vault_encrypted_unicode_4.upper()
            list_0 = []
            ansible_sequence_0 = module_0.AnsibleSequence(*list_0)
            var_2 = ansible_vault_encrypted_unicode_1.__lt__(ansible_sequence_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
