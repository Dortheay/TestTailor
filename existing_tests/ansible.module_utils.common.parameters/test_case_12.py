import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        str_0 = 'password'
        str_1 = 'config'
        str_2 = '_ansible_meta'
        str_3 = 'secret'
        str_4 = 'admin'
        str_5 = 'api_key'
        str_6 = 'endpoint'
        str_7 = 'private_key'
        str_8 = {str_5: str_7, str_6: str_2}
        str_9 = 'meta_info'
        str_10 = {str_0: str_3, str_0: str_4, str_1: str_8, str_2: str_9}
        str_11 = 'sanitized'
        str_12 = {str_3, str_7, str_11}
        str_13 = {str_2}
        var_0 = module_0.sanitize_keys(str_10, str_12, str_13)

if __name__ == "__main__":
    unittest.main()
