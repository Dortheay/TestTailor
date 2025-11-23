import unittest
import timeout_decorator
import dataclasses_json.core as module_0
import uuid as module_1

class Test_Core_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        extended_encoder_0 = module_0._ExtendedEncoder()
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = [int_0, int_1, int_2]
        var_0 = extended_encoder_0.default(int_3)
        str_0 = 'key'
        str_1 = 'value'
        str_2 = {str_0: str_1}
        var_1 = extended_encoder_0.default(str_2)
        str_3 = '12345678123456781234567812345678'
        u_u_i_d_0 = module_1.UUID(str_3)
        var_2 = extended_encoder_0.default(u_u_i_d_0)
        var_3 = str(u_u_i_d_0)

if __name__ == "__main__":
    unittest.main()
