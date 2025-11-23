import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = None
            var_0 = module_0.parse_kv(str_0, str_0)
            str_1 = 'G9pu>\nXc5cX2nM}'
            str_2 = '=4T*S%kvG6'
            var_1 = module_0.parse_kv(str_2)
            var_2 = module_0.parse_kv(str_1)
            bytes_0 = b''
            var_3 = module_0.parse_kv(bytes_0)
            str_3 = '\nw\x0ctQ{'
            var_4 = module_0.parse_kv(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
