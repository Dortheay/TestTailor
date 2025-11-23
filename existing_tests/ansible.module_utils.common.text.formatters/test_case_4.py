import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -440
            var_0 = module_0.bytes_to_human(int_0)
            bytes_0 = b'i\xdbLi\x8fg\xc2LE\xc7\xc0\xb0\xd8\xa4\x97\xe3,'
            dict_0 = {var_0: bytes_0}
            var_1 = module_0.human_to_bytes(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
