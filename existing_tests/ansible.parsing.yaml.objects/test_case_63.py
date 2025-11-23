import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_64(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_39(self):
        try:
            str_0 = 't^k$&FpT}&Fb=\\'
            list_0 = []
            bool_0 = True
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bool_0)
            var_0 = ansible_vault_encrypted_unicode_0.__str__()
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: list_0}
            list_1 = [dict_0, dict_0, dict_0]
            str_1 = 'n/a92z\rTE W#,5OZ%\n>'
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            var_1 = ansible_vault_encrypted_unicode_1.isdecimal()
            var_2 = ansible_vault_encrypted_unicode_1.isdigit()
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(str_1)
            var_3 = ansible_vault_encrypted_unicode_1.isupper()
            var_4 = ansible_vault_encrypted_unicode_2.__radd__(str_1)
            var_5 = ansible_vault_encrypted_unicode_2.isdigit()
            var_6 = ansible_vault_encrypted_unicode_0.partition(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
