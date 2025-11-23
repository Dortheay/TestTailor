import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_57(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        try:
            str_0 = '3Ky58/RMyAv(\\6ez<O'
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
            ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_1)
            var_0 = ansible_vault_encrypted_unicode_2.splitlines()
            var_1 = ansible_vault_encrypted_unicode_0.isidentifier()
            var_2 = ansible_vault_encrypted_unicode_0.islower()
            ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
            var_3 = ansible_vault_encrypted_unicode_0.__mod__(ansible_vault_encrypted_unicode_3)
            ansible_sequence_0 = module_0.AnsibleSequence()
            list_0 = [ansible_vault_encrypted_unicode_1, ansible_vault_encrypted_unicode_2]
            ansible_vault_encrypted_unicode_4 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_4 = ansible_vault_encrypted_unicode_0.__mod__(ansible_vault_encrypted_unicode_4)
            var_5 = ansible_vault_encrypted_unicode_0.isprintable()
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
            list_1 = [ansible_vault_encrypted_unicode_1, ansible_sequence_0, ansible_sequence_0]
            var_6 = ansible_vault_encrypted_unicode_1.__getitem__(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
