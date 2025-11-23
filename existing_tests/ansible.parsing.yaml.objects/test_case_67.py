import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_68(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_43(self):
        try:
            bool_0 = True
            list_0 = [bool_0, bool_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_0 = ansible_vault_encrypted_unicode_0.isnumeric()
            dict_0 = {}
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            var_1 = ansible_vault_encrypted_unicode_1.__str__()
            str_0 = ' ode'
            set_0 = {str_0, str_0, str_0}
            list_1 = [var_1, var_1]
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            var_2 = ansible_vault_encrypted_unicode_2.isalnum()
            var_3 = ansible_vault_encrypted_unicode_1.__radd__(set_0)
            str_1 = 'SRvdI3Hy\\eBLBO)q\t*AJ'
            int_0 = 304
            var_4 = ansible_vault_encrypted_unicode_2.__gt__(str_1)
            ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            bytes_0 = b'G&'
            var_5 = ansible_vault_encrypted_unicode_3.__add__(bytes_0)
            var_6 = ansible_vault_encrypted_unicode_3.lstrip()
            str_2 = 'bNrgs?Dp\r'
            str_3 = '^c_fgAR7'
            int_1 = 912
            var_7 = ansible_vault_encrypted_unicode_3.__ne__(int_1)
            var_8 = ansible_vault_encrypted_unicode_3.__contains__(str_3)
            str_4 = 'n8H8}'
            ansible_unicode_0 = module_0.AnsibleUnicode()
            var_9 = ansible_vault_encrypted_unicode_1.__eq__(ansible_unicode_0)
            var_10 = ansible_vault_encrypted_unicode_2.isprintable()
            dict_1 = {str_3: var_9, str_1: bytes_0, str_1: str_1, str_2: str_2, str_4: str_1}
            ansible_mapping_0 = module_0.AnsibleMapping(**dict_1)
            list_2 = [ansible_vault_encrypted_unicode_3, var_1, str_2, ansible_mapping_0]
            ansible_vault_encrypted_unicode_4 = module_0.AnsibleVaultEncryptedUnicode(list_2)
            ansible_vault_encrypted_unicode_5 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            var_11 = ansible_vault_encrypted_unicode_5.isascii()
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
            var_12 = ansible_vault_encrypted_unicode_5.count(ansible_vault_encrypted_unicode_2)
            ansible_sequence_0 = module_0.AnsibleSequence(*list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
