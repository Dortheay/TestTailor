import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        str_0 = ' ode'
        str_1 = 'SRvdI3Hy\\eBLBO)q\t*AJ'
        int_0 = 304
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
        bytes_0 = b'G&'
        var_0 = ansible_vault_encrypted_unicode_0.__add__(bytes_0)
        var_1 = ansible_vault_encrypted_unicode_0.lstrip()
        str_2 = 'bNrgs?Dp\r'
        str_3 = '^c_fgAR7'
        var_2 = ansible_vault_encrypted_unicode_0.__contains__(str_3)
        dict_0 = {str_1: str_1, str_2: str_2, str_0: str_1}
        ansible_mapping_0 = module_0.AnsibleMapping(**dict_0)
        ansible_unicode_0 = module_0.AnsibleUnicode()

if __name__ == "__main__":
    unittest.main()
