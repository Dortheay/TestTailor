import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0

class Test_Objects_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '346.073'
        ansible_mapping_0 = module_0.AnsibleMapping()
        int_0 = -2675
        str_1 = 'Skipping unexpected key (%s) in group (%s), only "vars", "children" and "hosts" are valid'
        str_2 = None
        dict_0 = {str_1: str_1, str_2: str_2, str_1: str_0, str_2: str_2}
        ansible_sequence_0 = module_0.AnsibleSequence(**dict_0)
        ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_sequence_0)
        var_0 = ansible_vault_encrypted_unicode_0.__add__(int_0)
        ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
        var_1 = ansible_vault_encrypted_unicode_1.__contains__(str_0)

if __name__ == "__main__":
    unittest.main()
