import unittest
import timeout_decorator
import ansible.constants as module_0

class Test_Constants_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            int_0 = 3310
            bytes_0 = b'\xf7\xea$Zl?a\xa5jF'
            bytes_1 = b'\x00'
            list_0 = None
            list_1 = [list_0, int_0, int_0, bytes_1]
            tuple_0 = (bytes_0, bytes_1, list_1)
            dict_0 = {list_0: tuple_0, bytes_1: tuple_0}
            deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(int_0, tuple_0, dict_0)
            var_0 = deprecated_sequence_constant_0.__getitem__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
