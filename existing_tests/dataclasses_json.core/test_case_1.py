import unittest
import timeout_decorator
import dataclasses_json.core as module_0
import uuid as module_1

class Test_Core_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        extended_encoder_0 = module_0._ExtendedEncoder()
        bytes_0 = b's\x19\xb69\x12'
        int_0 = 3567
        str_0 = None
        dict_0 = {str_0: str_0}
        var_0 = extended_encoder_0.default(dict_0)
        extended_encoder_1 = module_0._ExtendedEncoder(skipkeys=bytes_0, allow_nan=int_0)

if __name__ == "__main__":
    unittest.main()
