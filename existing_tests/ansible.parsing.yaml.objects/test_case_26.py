import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'\xe4\xc6\xe4_z'
            list_0 = [bytes_0, bytes_0]
            dict_0 = {}
            ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject(**dict_0)
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_base_y_a_m_l_object_0)
            var_0 = ansible_vault_encrypted_unicode_0.encode(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
