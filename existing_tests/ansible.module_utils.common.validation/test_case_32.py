import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        try:
            bytes_0 = b"+\xc4\xf6E\x16R\x95\x0c\x16\xfe\xc1\xdcu\x05\t\x06\xd4'\x06\xba"
            var_0 = module_0.check_missing_parameters(bytes_0)
            str_0 = ''
            complex_0 = None
            var_1 = module_0.safe_eval(str_0, complex_0)
            int_0 = None
            float_0 = 2968.2089
            var_2 = module_0.check_type_str(float_0)
            bytes_1 = b'\x8a@\r|\xce\xae8\xf5Gr\xc4[~'
            str_1 = 'N'
            list_0 = [bytes_1, str_1, float_0, complex_0]
            var_3 = module_0.safe_eval(bytes_1, str_1, list_0)
            tuple_0 = ()
            bool_0 = False
            float_1 = 1837.195847
            set_0 = {float_1, complex_0}
            tuple_1 = (tuple_0, int_0, bool_0, set_0)
            var_4 = module_0.check_type_list(tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
