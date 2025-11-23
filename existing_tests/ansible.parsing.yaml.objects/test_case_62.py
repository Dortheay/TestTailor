import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_63(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_38(self):
        try:
            dict_0 = {}
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            var_0 = ansible_vault_encrypted_unicode_0.__str__()
            str_0 = ' ode'
            set_0 = {str_0, str_0, str_0}
            dict_1 = {}
            var_1 = ansible_vault_encrypted_unicode_0.isalpha()
            list_0 = [var_0, var_0]
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_2 = ansible_vault_encrypted_unicode_1.isalnum()
            var_3 = ansible_vault_encrypted_unicode_0.__radd__(set_0)
            int_0 = 304
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            bytes_0 = b'G&'
            var_4 = ansible_vault_encrypted_unicode_2.__add__(bytes_0)
            var_5 = ansible_vault_encrypted_unicode_2.lstrip()
            str_1 = '@%<NdHc b:'
            var_6 = ansible_vault_encrypted_unicode_2.__ge__(str_1)
            str_2 = '^c_fgAR7'
            var_7 = ansible_vault_encrypted_unicode_2.__contains__(str_2)
            tuple_0 = None
            ansible_mapping_0 = module_0.AnsibleMapping(**dict_1)
            var_8 = ansible_vault_encrypted_unicode_1.find(tuple_0, ansible_mapping_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
