import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            ansible_mapping_0 = module_0.AnsibleMapping()
            str_0 = 'Path %s is owned by uid %s, not by uid %s as expected\n'
            int_0 = -809
            dict_0 = {int_0: int_0}
            float_0 = 165.1
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(float_0)
            var_0 = ansible_vault_encrypted_unicode_0.__complex__()
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            var_1 = ansible_vault_encrypted_unicode_1.startswith(ansible_mapping_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
