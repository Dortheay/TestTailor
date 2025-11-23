import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'Y'
            var_0 = module_0.parse_kv(str_0, str_0)
            str_1 = '=4T*S%kvG6'
            var_1 = module_0.parse_kv(str_1)
            str_2 = '&{"\nM8j:+Uu\\'
            var_2 = module_0.parse_kv(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
