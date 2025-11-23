import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        dict_0 = {}
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
        var_0 = ansible_vault_encrypted_unicode_0.__str__()
        str_0 = ' ode'
        set_0 = {str_0, str_0, str_0}
        list_0 = [var_0, var_0]
        var_1 = ansible_vault_encrypted_unicode_0.isalnum()
        var_2 = ansible_vault_encrypted_unicode_0.__radd__(set_0)
        str_1 = 'SRvdI3Hy\\eBLBO)q\t*AJ'
        int_0 = 304
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(int_0)
        bytes_0 = b'G&\xbb\x0e'
        var_3 = ansible_vault_encrypted_unicode_1.__add__(bytes_0)
        var_4 = ansible_vault_encrypted_unicode_1.lstrip()
        str_2 = 'bNrgs?Dp\r'
        str_3 = '^c_fgAR7'
        int_1 = 912
        var_5 = ansible_vault_encrypted_unicode_1.__ne__(int_1)
        var_6 = ansible_vault_encrypted_unicode_1.__contains__(str_3)
        str_4 = 'n8H8}'
        ansible_unicode_0 = module_0.AnsibleUnicode()
        var_7 = ansible_vault_encrypted_unicode_0.__eq__(ansible_unicode_0)
        dict_1 = {str_1: str_1, str_2: str_2, str_4: str_1}
        ansible_mapping_0 = module_0.AnsibleMapping(**dict_1)
        list_1 = [ansible_vault_encrypted_unicode_1, var_0, str_2, ansible_mapping_0]
        ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(list_1)
        var_8 = ansible_vault_encrypted_unicode_2.__reversed__()
        ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(list_0)
        var_9 = ansible_vault_encrypted_unicode_3.isascii()
        ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
        str_5 = 'vHZcQ04V4EJ'
        dict_2 = {str_5: ansible_mapping_0}
        list_2 = [ansible_base_y_a_m_l_object_0, list_1, dict_2, list_0]
        ansible_vault_encrypted_unicode_4 = module_0.AnsibleVaultEncryptedUnicode(list_2)
        ansible_base_y_a_m_l_object_1 = module_0.AnsibleBaseYAMLObject()
        var_10 = ansible_vault_encrypted_unicode_4.__le__(ansible_vault_encrypted_unicode_3)

if __name__ == "__main__":
    unittest.main()
