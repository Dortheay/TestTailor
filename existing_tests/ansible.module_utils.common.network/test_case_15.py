import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = '255.255.255.0'
            var_0 = module_0.to_bits(str_0)
            str_1 = '255.255.0.0'
            var_1 = module_0.to_bits(str_1)
            str_2 = '255.0.0.0'
            var_2 = module_0.to_bits(str_2)
            str_3 = '0.0.0.0'
            var_3 = module_0.to_bits(str_3)
            str_4 = '255.128.0.0'
            var_4 = module_0.to_bits(str_4)
            str_5 = '255.255.255.255'
            var_5 = module_0.to_bits(str_5)
            str_6 = 'invalid.input'
            var_6 = module_0.to_bits(str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
