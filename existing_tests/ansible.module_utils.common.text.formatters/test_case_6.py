import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = -440
            str_0 = '3k_0)'
            complex_0 = None
            var_0 = module_0.human_to_bytes(str_0, complex_0)
            var_1 = module_0.bytes_to_human(int_0)
            float_0 = 29.825033266052387
            var_2 = module_0.human_to_bytes(float_0)
            bytes_0 = b'i\xdbLi\x8fg\xc2LE\xc7\xc0\xb0\xd8\xa4\x97\xe3,'
            set_0 = set()
            list_0 = [bytes_0, var_2, var_1]
            var_3 = module_0.lenient_lowercase(list_0)
            tuple_0 = (int_0, set_0, bytes_0)
            var_4 = module_0.lenient_lowercase(tuple_0)
            bytes_1 = b'\xa6\x18\x94'
            var_5 = module_0.lenient_lowercase(bytes_1)
            dict_0 = {}
            var_6 = module_0.bytes_to_human(int_0, dict_0)
            dict_1 = None
            tuple_1 = (dict_1,)
            var_7 = module_0.human_to_bytes(tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
