import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = False
            bytes_0 = b'\xdb\x86\t'
            var_0 = module_0.do_unvault(bool_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
