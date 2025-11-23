import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_62(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_37(self):
        try:
            dict_0 = {}
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            var_0 = ansible_vault_encrypted_unicode_0.__str__()
            str_0 = ' ode'
            set_0 = {str_0, str_0, str_0}
            dict_1 = {str_0: set_0, str_0: str_0, str_0: str_0}
            list_0 = [var_0, var_0]
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_1 = ansible_vault_encrypted_unicode_1.isalnum()
            str_1 = 'SRvdI3Hy\\eBLBO)q\t*AJ'
            list_1 = [dict_1, set_0, dict_0]
            var_2 = ansible_vault_encrypted_unicode_1.__eq__(list_1)
            int_0 = 304
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            bytes_0 = b'G&'
            var_3 = ansible_vault_encrypted_unicode_2.__add__(bytes_0)
            var_4 = ansible_vault_encrypted_unicode_2.lstrip()
            str_2 = 'bNrgs?Dp\r'
            var_5 = ansible_vault_encrypted_unicode_2.__reversed__()
            str_3 = '^c_fgAR7'
            var_6 = ansible_vault_encrypted_unicode_0.is_encrypted()
            var_7 = ansible_vault_encrypted_unicode_2.__contains__(str_3)
            str_4 = '8H}'
            dict_2 = {str_1: str_1, str_2: str_2, str_4: str_1}
            var_8 = ansible_vault_encrypted_unicode_0.format(*list_1, **dict_2)
            ansible_mapping_0 = module_0.AnsibleMapping(**dict_2)
            ansible_base_y_a_m_l_object_0 = None
            tuple_0 = (ansible_vault_encrypted_unicode_1, set_0, ansible_base_y_a_m_l_object_0)
            var_9 = ansible_vault_encrypted_unicode_0.__gt__(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
