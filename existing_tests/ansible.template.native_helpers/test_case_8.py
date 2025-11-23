import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0
import jinja2.runtime as module_1
import ansible.parsing.yaml.objects as module_2

class Test_Native_helpers_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 42
            int_1 = [int_0]
            var_0 = module_0.ansible_native_concat(int_1)
            str_0 = 'secret'
            ansible_vault_encrypted_unicode_0 = module_2.AnsibleVaultEncryptedUnicode(str_0)
            ansible_vault_encrypted_unicode_1 = [ansible_vault_encrypted_unicode_0]
            var_1 = module_0.ansible_native_concat(ansible_vault_encrypted_unicode_1)
            str_1 = '1'
            str_2 = '+'
            str_3 = '2'
            str_4 = [str_1, str_2, str_3]
            var_2 = module_0.ansible_native_concat(str_4)
            strict_undefined_0 = module_1.StrictUndefined()
            str_5 = 'key'
            strict_undefined_1 = {str_5: strict_undefined_0}
            int_2 = [int_0]
            str_6 = 'value'
            var_3 = [strict_undefined_1, int_2, str_6]
            var_4 = module_0.ansible_native_concat(var_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
