import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_67(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_42(self):
        try:
            dict_0 = {}
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            var_0 = ansible_vault_encrypted_unicode_0.__str__()
            str_0 = ' ode'
            set_0 = {str_0, str_0, str_0}
            var_1 = ansible_vault_encrypted_unicode_0.expandtabs()
            list_0 = [var_0, var_0]
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_2 = ansible_vault_encrypted_unicode_1.isalnum()
            var_3 = ansible_vault_encrypted_unicode_0.__radd__(set_0)
            int_0 = 304
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(int_0)
            var_4 = ansible_vault_encrypted_unicode_2.__add__(ansible_vault_encrypted_unicode_0)
            var_5 = ansible_vault_encrypted_unicode_2.lstrip()
            str_1 = '^c_fgAR7'
            int_1 = 912
            var_6 = ansible_vault_encrypted_unicode_2.__ne__(int_1)
            var_7 = ansible_vault_encrypted_unicode_2.__contains__(str_1)
            ansible_unicode_0 = module_0.AnsibleUnicode()
            var_8 = ansible_vault_encrypted_unicode_2.__hash__()
            var_9 = ansible_vault_encrypted_unicode_1.__int__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
