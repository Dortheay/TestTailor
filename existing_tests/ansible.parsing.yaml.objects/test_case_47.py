import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_48(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            bool_0 = True
            ansible_sequence_0 = module_0.AnsibleSequence()
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_sequence_0)
            var_0 = ansible_vault_encrypted_unicode_0.rindex(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
