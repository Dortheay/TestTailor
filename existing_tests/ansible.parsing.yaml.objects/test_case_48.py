import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_49(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            str_0 = '`+&1S5\naZ`w/}'
            list_0 = None
            list_1 = [list_0, list_0, list_0, list_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            var_0 = ansible_vault_encrypted_unicode_0.rjust(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
