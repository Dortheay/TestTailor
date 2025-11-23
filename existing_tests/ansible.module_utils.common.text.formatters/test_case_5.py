import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = 0.0
            var_0 = module_0.human_to_bytes(float_0)
            bytes_0 = b'i\xdbLi\x8fg\xc2LE\xc7\xc0\xb0\xd8\xa4\x97\xe3,'
            var_1 = module_0.lenient_lowercase(bytes_0)
            str_0 = '2S\x0b\x0cVW<hiz1'
            var_2 = module_0.human_to_bytes(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
