import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'ansible.plugins.become'
            int_0 = None
            filter_module_0 = None
            int_1 = None
            tuple_0 = (filter_module_0, int_1)
            set_0 = set()
            bytes_0 = b'O\x07\x9f\xb4\x1f>\x82\xfct\x9d'
            var_0 = module_0.do_vault(str_0, int_0, tuple_0, set_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
