import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        bool_0 = True
        bytes_0 = b"'\x8b\xbd\xfe\xd2\x04\xc6\xb69\xc2\xbd\x904f\x8c\xf9\xc8"
        validation_0 = module_0.Validation(bool_0, bytes_0)
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
        bool_1 = False
        validation_1 = module_0.Validation(dict_0, bool_1)
        var_0 = validation_1.__eq__(validation_0)

if __name__ == "__main__":
    unittest.main()
