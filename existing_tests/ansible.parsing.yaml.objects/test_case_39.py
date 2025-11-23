import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            float_0 = 3230.554913
            ansible_sequence_0 = module_0.AnsibleSequence()
            dict_0 = {}
            str_0 = 'D,VBb8\n'
            tuple_0 = (ansible_sequence_0, dict_0, str_0)
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(tuple_0)
            var_0 = ansible_vault_encrypted_unicode_0.__rmod__(float_0)
            float_1 = 699.0
            var_1 = ansible_vault_encrypted_unicode_0.__le__(float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
