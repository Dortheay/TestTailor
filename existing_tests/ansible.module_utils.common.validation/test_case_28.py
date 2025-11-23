import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_28(self):
        try:
            list_0 = []
            dict_0 = None
            bool_0 = False
            var_0 = module_0.check_required_arguments(dict_0, bool_0)
            tuple_0 = None
            var_1 = module_0.check_required_if(list_0, tuple_0)
            float_0 = -4413.5213
            str_0 = 'W@i)TNz`@\r@%\\FJ'
            var_2 = module_0.check_required_together(list_0, float_0, str_0)
            bytes_0 = b'\xc7\xb7\x83g1\xc6\xb8K\xea\xd4\xca\xb6\x81P]\x14\x94\xf9\xff'
            str_1 = '}pcECqz'
            var_3 = module_0.check_type_str(bytes_0, str_0, str_1)
            str_2 = 't/M"g^rq.}4LNPN=M<x'
            var_4 = module_0.check_type_float(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
