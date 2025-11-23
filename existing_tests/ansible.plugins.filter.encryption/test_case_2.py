import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x05\x93\xe69\x11C'
            str_0 = ']pux(\\B8Q3m'
            var_0 = module_0.do_vault(bytes_0, str_0)
            bool_0 = False
            bool_1 = False
            var_1 = module_0.do_unvault(bool_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
