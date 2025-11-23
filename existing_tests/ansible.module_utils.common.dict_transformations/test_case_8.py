import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bytes_0 = b'\x1f\xb4\x91\xd6\xf7\x04'
            str_0 = 'ZGQ]p'
            str_1 = '*tNm {U&\\D$\r5}"(T\x0c'
            str_2 = 'facts'
            var_0 = module_0.snake_dict_to_camel_dict(str_1, str_2)
            bool_0 = None
            dict_0 = {var_0: str_0, bytes_0: bytes_0, bool_0: str_2, bool_0: str_2}
            dict_1 = {}
            var_1 = module_0.recursive_diff(dict_0, dict_1)
            float_0 = -1601.4380923575575
            dict_2 = {float_0: str_2}
            bool_1 = False
            var_2 = module_0.recursive_diff(dict_2, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
