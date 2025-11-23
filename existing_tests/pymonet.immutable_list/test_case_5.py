import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b''
            float_0 = 664.53728
            bytes_1 = b'\xc7Vq\xb5'
            bool_0 = True
            immutable_list_0 = module_0.ImmutableList(float_0, bytes_1, bool_0)
            var_0 = immutable_list_0.map(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
