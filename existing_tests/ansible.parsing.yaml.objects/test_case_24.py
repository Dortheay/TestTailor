import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '\n    Converts an object into a dict making the properties into eys, allows exclu9ingbcertain keys\n    '
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
            var_0 = ansible_vault_encrypted_unicode_0.__reversed__()
            var_1 = ansible_vault_encrypted_unicode_0.__add__(str_0)
            float_0 = 0.1
            ansible_sequence_0 = module_0.AnsibleSequence()
            tuple_0 = (ansible_sequence_0,)
            var_2 = ansible_vault_encrypted_unicode_0.startswith(float_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
