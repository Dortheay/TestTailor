import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_51(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            float_0 = -1291.84717
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(float_0)
            var_0 = ansible_vault_encrypted_unicode_0.title()
            var_1 = ansible_vault_encrypted_unicode_0.isdigit()
            var_2 = ansible_vault_encrypted_unicode_0.rstrip()
            bytes_0 = b'\x11x\x1e>B\xd2\xfb'
            var_3 = ansible_vault_encrypted_unicode_0.replace(ansible_vault_encrypted_unicode_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
