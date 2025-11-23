import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'test_data'
            str_1 = 'test_secret'
            str_2 = 'test_salt'
            str_3 = 'test_vaultid'
            bool_0 = True
            var_0 = module_0.do_vault(str_0, str_1, str_2, str_3, bool_0)
            bool_1 = False
            var_1 = module_0.do_vault(str_0, str_1, str_2, str_3, bool_1)
            int_0 = 12345
            var_2 = module_0.do_vault(str_0, int_0, str_2, str_3, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
