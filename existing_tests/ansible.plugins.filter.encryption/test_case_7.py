import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'valid_secret'
            str_1 = 'test_data'
            var_0 = module_0.do_vault(str_1, str_0)
            bytes_0 = b'$ANSIBLE_VAULT;1.1;AES256\nabc123'
            var_1 = module_1.to_text(bytes_0)
            str_2 = 'invalid_secret'
            var_2 = module_0.do_vault(str_1, str_2)
            str_3 = 'valid_secret'
            int_0 = 12345
            var_3 = module_0.do_vault(int_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
