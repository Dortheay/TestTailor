import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'my_secret'
            str_1 = '$ANSIBLE_VAULT;1.1;AES256\nencrypted_content'
            str_2 = 'filter_default'
            var_0 = module_1.to_bytes(str_0)
            vault_secret_0 = module_2.VaultSecret(var_0)
            var_1 = module_0.do_unvault(str_1, str_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
