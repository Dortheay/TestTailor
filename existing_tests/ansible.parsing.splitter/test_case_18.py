import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'Y'
            str_1 = None
            var_0 = module_0.parse_kv(str_1, str_1)
            str_2 = '=4T*S%kvG6'
            str_3 = "+_' '=QQ"
            var_1 = module_0.parse_kv(str_3)
            dict_0 = {str_0: str_2, str_3: str_0, str_3: str_3, str_0: str_0}
            var_2 = module_0.parse_kv(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
