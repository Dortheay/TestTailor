import unittest
import timeout_decorator
import dataclasses_json.core as module_0
import uuid as module_1

class Test_Core_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        list_0 = []
        extended_encoder_0 = module_0._ExtendedEncoder(ensure_ascii=list_0)
        str_0 = 'Bza]-Y1i!iyj'
        var_0 = extended_encoder_0.default(str_0)

if __name__ == "__main__":
    unittest.main()
