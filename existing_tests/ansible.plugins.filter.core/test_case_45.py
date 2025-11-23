import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_45(self):
        try:
            str_0 = '\no\t9\nMdG&GA'
            bytes_0 = b'\x80\xc1\xf5\xa2\x85\xb7\xe0\xc5'
            str_1 = '+I(6x\rnfWuk8mb]\\z@c'
            dict_0 = {str_1: str_1, str_0: str_0}
            str_2 = None
            dict_1 = {str_2: str_0}
            var_0 = module_0.to_yaml(dict_1)
            var_1 = module_0.rand(str_0, bytes_0, str_1, bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
