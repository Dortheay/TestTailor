import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = 'A}1.82A>2(\rpO*0'
            ansible_unicode_0 = module_0.AnsibleUnicode()
            list_0 = []
            bool_0 = False
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_base_y_a_m_l_object_0)
            var_0 = ansible_vault_encrypted_unicode_0.rstrip()
            var_1 = ansible_vault_encrypted_unicode_0.__reversed__()
            str_1 = 'D-(.A3)}'
            set_0 = set()
            var_2 = ansible_vault_encrypted_unicode_0.join(set_0)
            var_3 = ansible_vault_encrypted_unicode_0.istitle()
            str_2 = 'Csd,@n8$\tF!dX-c'
            dict_0 = {str_2: str_0}
            dict_1 = {str_1: dict_0}
            ansible_sequence_0 = module_0.AnsibleSequence(**dict_1)
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(bool_0)
            var_4 = ansible_vault_encrypted_unicode_1.split(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
