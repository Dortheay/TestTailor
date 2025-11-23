import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            bytes_0 = b'\\\x9f\x91D;F\xb0-$BY\x8c\xdf\xabx\xc2\xa9\x91'
            str_0 = '6O^R '
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
            var_0 = ansible_vault_encrypted_unicode_0.__ge__(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
