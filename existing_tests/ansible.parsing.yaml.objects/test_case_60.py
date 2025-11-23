import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_61(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_36(self):
        try:
            str_0 = '[R5'
            list_0 = [str_0, str_0, str_0]
            bool_0 = True
            list_1 = [bool_0, bool_0, bool_0, bool_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            var_0 = ansible_vault_encrypted_unicode_0.ljust(str_0, *list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
