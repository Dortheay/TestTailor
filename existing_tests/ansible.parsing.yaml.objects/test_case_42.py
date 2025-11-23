import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = ''
            list_0 = [str_0]
            str_1 = '2p{H<uIF7'
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_1)
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
            var_0 = ansible_vault_encrypted_unicode_1.__radd__(list_0)
            str_2 = 'magenta'
            dict_0 = {str_0: str_0, str_2: str_2}
            complex_0 = None
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
            bytes_0 = b'&\xf0\xcf\xd0\xe1O'
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
            ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_2)
            var_1 = ansible_vault_encrypted_unicode_3.endswith(str_2)
            ansible_vault_encrypted_unicode_4 = module_0.AnsibleVaultEncryptedUnicode(ansible_base_y_a_m_l_object_0)
            var_2 = ansible_vault_encrypted_unicode_4.index(dict_0, complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
