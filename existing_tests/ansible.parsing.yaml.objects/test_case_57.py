import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_58(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            int_0 = -607
            dict_0 = {int_0: int_0}
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
            var_0 = ansible_vault_encrypted_unicode_0.casefold()
            list_0 = []
            var_1 = ansible_vault_encrypted_unicode_0.startswith(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
