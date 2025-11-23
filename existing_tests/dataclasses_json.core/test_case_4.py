import unittest
import timeout_decorator
import dataclasses_json.core as module_0

class Test_Core_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -743.8010015951345
            extended_encoder_0 = module_0._ExtendedEncoder(check_circular=float_0, sort_keys=float_0)
            var_0 = extended_encoder_0.default(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
