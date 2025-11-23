import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_65(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_40(self):
        try:
            dict_0 = {}
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            var_0 = ansible_vault_encrypted_unicode_0.__str__()
            str_0 = ' ode'
            set_0 = {str_0, str_0, str_0}
            list_0 = [var_0, var_0]
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_1 = ansible_vault_encrypted_unicode_1.isalnum()
            var_2 = ansible_vault_encrypted_unicode_0.__radd__(set_0)
            str_1 = 'SRvdI3Hy\\eBLBO)q\t*AJ'
            int_0 = 304
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            bytes_0 = b'G&'
            var_3 = ansible_vault_encrypted_unicode_2.__add__(bytes_0)
            var_4 = ansible_vault_encrypted_unicode_2.lstrip()
            str_2 = 'bNrgs?Dp\r'
            str_3 = '^c_fgAR7'
            var_5 = ansible_vault_encrypted_unicode_2.__contains__(str_3)
            str_4 = '8H}'
            dict_1 = {str_1: str_1, str_2: str_2, str_4: str_1}
            ansible_mapping_0 = module_0.AnsibleMapping(**dict_1)
            list_1 = [ansible_vault_encrypted_unicode_2, var_0, str_2, ansible_mapping_0]
            ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            var_6 = ansible_vault_encrypted_unicode_3.__reversed__()
            ansible_sequence_0 = module_0.AnsibleSequence()
            int_1 = -2125
            tuple_0 = (ansible_sequence_0, int_1)
            ansible_vault_encrypted_unicode_4 = module_0.AnsibleVaultEncryptedUnicode(tuple_0)
            float_0 = 1501.5299
            ansible_vault_encrypted_unicode_5 = module_0.AnsibleVaultEncryptedUnicode(float_0)
            var_7 = ansible_vault_encrypted_unicode_5.isascii()
            ansible_unicode_0 = module_0.AnsibleUnicode()
            float_1 = 2086.5
            var_8 = ansible_vault_encrypted_unicode_1.replace(float_1, ansible_vault_encrypted_unicode_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
