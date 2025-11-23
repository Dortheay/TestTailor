import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'dummy_secret'
            str_1 = 'filter_default'
            var_0 = module_1.to_bytes(str_0)
            vault_secret_0 = module_2.VaultSecret(var_0)
            var_1 = (str_1, vault_secret_0)
            var_2 = [var_1]
            vault_lib_0 = module_2.VaultLib(var_2)
            var_3 = module_0.do_unvault(str_0, str_0, str_1)
            str_2 = 'plain_text_data'
            var_4 = module_0.do_unvault(str_2, str_0)
            ansible_vault_encrypted_unicode_0 = module_3.AnsibleVaultEncryptedUnicode(str_1)
            var_5 = module_0.do_unvault(ansible_vault_encrypted_unicode_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
