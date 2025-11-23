import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            list_0 = []
            list_1 = [list_0, list_0]
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_1)
            var_0 = ansible_vault_encrypted_unicode_0.__float__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
