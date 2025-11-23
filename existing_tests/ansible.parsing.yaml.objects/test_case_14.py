import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        dict_0 = {}
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
        var_0 = ansible_vault_encrypted_unicode_0.__str__()
        list_0 = [var_0, var_0]
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_0)
        var_1 = ansible_vault_encrypted_unicode_1.isalnum()
        str_0 = 'SRvdI3Hy\\eBLBO)q\t*AJ'
        int_0 = 304
        ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(int_0)
        bytes_0 = b'G&'
        var_2 = ansible_vault_encrypted_unicode_2.__add__(bytes_0)
        var_3 = ansible_vault_encrypted_unicode_2.lstrip()
        str_1 = 'bNrgs?Dp\r'
        str_2 = '^c_fgAR7'
        var_4 = ansible_vault_encrypted_unicode_2.__contains__(str_2)
        str_3 = '8H}'
        dict_1 = {str_0: str_0, str_1: str_1, str_2: bytes_0, str_1: str_0, str_3: str_0}
        ansible_mapping_0 = module_0.AnsibleMapping(**dict_1)
        list_1 = [ansible_vault_encrypted_unicode_2, var_0, str_1, ansible_mapping_0]
        ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(list_1)
        var_5 = ansible_vault_encrypted_unicode_1.__reversed__()
        ansible_vault_encrypted_unicode_4 = module_0.AnsibleVaultEncryptedUnicode(list_0)
        var_6 = ansible_vault_encrypted_unicode_4.isascii()
        ansible_unicode_0 = module_0.AnsibleUnicode()
        int_1 = 659
        var_7 = ansible_vault_encrypted_unicode_2.replace(ansible_vault_encrypted_unicode_0, ansible_unicode_0, int_1)

if __name__ == "__main__":
    unittest.main()
