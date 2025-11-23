import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            bytes_0 = b'<\xddc\x8f(S\xda'
            var_0 = module_0.fileglob(bytes_0)
            bool_0 = False
            var_1 = module_0.quote(bool_0)
            str_0 = 'posix_basic'
            dict_0 = {str_0: str_0, str_0: bytes_0}
            var_2 = module_0.list_of_dict_key_value_elements_to_dict(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
