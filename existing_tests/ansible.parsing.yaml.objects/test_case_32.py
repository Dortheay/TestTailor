import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'sGW$o\r|MkL`a9Sy'
            tuple_0 = (str_0, str_0)
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(tuple_0)
            var_0 = ansible_vault_encrypted_unicode_0.isdigit()
            ansible_unicode_0 = module_0.AnsibleUnicode()
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
            list_0 = [ansible_unicode_0, ansible_unicode_0, ansible_unicode_0]
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(list_0)
            var_1 = ansible_vault_encrypted_unicode_1.__add__(str_0)
            var_2 = ansible_vault_encrypted_unicode_1.__lt__(ansible_vault_encrypted_unicode_1)
            list_1 = [ansible_unicode_0, ansible_unicode_0, ansible_unicode_0]
            ansible_base_y_a_m_l_object_1 = module_0.AnsibleBaseYAMLObject(*list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
