import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_53(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_28(self):
        try:
            float_0 = -2897.1
            dict_0 = {float_0: float_0}
            ansible_mapping_0 = module_0.AnsibleMapping()
            set_0 = {float_0}
            str_0 = '$:n i,Xpt'
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
            var_0 = ansible_vault_encrypted_unicode_0.__radd__(set_0)
            ansible_sequence_0 = module_0.AnsibleSequence()
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
            var_1 = ansible_vault_encrypted_unicode_1.splitlines()
            var_2 = ansible_vault_encrypted_unicode_1.strip(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
