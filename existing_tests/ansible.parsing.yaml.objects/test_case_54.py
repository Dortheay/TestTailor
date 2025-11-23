import unittest
import timeout_decorator
import ansible.parsing.yaml.objects as module_0
import ansible.module_utils.common.text.converters as module_1

class Test_Objects_55(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            str_0 = 'z<BO|@m\t.#'
            int_0 = None
            str_1 = '4'
            str_2 = "0'#)--Q%<G1%A*"
            dict_0 = {str_0: str_0, str_0: int_0, str_1: str_0, str_2: str_0}
            ansible_sequence_0 = module_0.AnsibleSequence(**dict_0)
            ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_sequence_0)
            var_0 = ansible_vault_encrypted_unicode_0.swapcase()
            dict_1 = {int_0: str_2}
            set_0 = {str_0}
            ansible_unicode_0 = module_0.AnsibleUnicode()
            ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
            var_1 = ansible_vault_encrypted_unicode_1.title()
            var_2 = ansible_vault_encrypted_unicode_0.replace(dict_1, set_0, ansible_unicode_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
