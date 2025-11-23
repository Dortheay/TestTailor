import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'PSRP_RC{X%d'
            list_0 = [str_0]
            dict_0 = {str_0: list_0}
            var_0 = module_0.snake_dict_to_camel_dict(dict_0)
            var_1 = module_0.camel_dict_to_snake_dict(dict_0)
            bytes_0 = b'\xb3\x16\xc1\xad\xe0\x99\xcf\x9f*\xe9\xc3'
            tuple_0 = (str_0, bytes_0)
            int_0 = -82
            var_2 = module_0.camel_dict_to_snake_dict(tuple_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
