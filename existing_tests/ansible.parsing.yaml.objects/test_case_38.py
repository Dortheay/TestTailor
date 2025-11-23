import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            list_0 = []
            list_1 = [list_0, list_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            str_0 = 'bG$Oh'
            dict_0 = {str_0: list_0}
            ansible_mapping_0 = module_0.AnsibleMapping(**dict_0)
            var_0 = ansible_vault_encrypted_unicode_0.__mod__(ansible_mapping_0)
            ansible_unicode_0 = module_0.AnsibleUnicode()
            var_1 = ansible_vault_encrypted_unicode_0.rfind(ansible_unicode_0)
            var_2 = ansible_vault_encrypted_unicode_0.lower()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
