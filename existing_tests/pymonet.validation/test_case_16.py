import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        bytes_0 = b'#\x94\xf2\x81\xd8\x8a;B\xa2\x04\xa0\xa5\x10\x02\xef\x9d\xdc'
        validation_0 = module_0.Validation(bytes_0, bytes_0)
        var_0 = validation_0.is_fail()
        var_1 = validation_0.__str__()
        var_2 = validation_0.to_lazy()
        var_3 = validation_0.to_maybe()
        var_4 = validation_0.__eq__(validation_0)
        var_5 = validation_0.is_fail()

if __name__ == "__main__":
    unittest.main()
