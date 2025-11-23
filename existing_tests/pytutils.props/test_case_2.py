import unittest
import timeout_decorator
import pytutils.props as module_0

class Test_Props_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = -1102.0
            bytes_0 = b'B8\x14%\x05k\xa4\xc3*q\x03\xa6\xefk\xd0\x90\x99\xed'
            dict_0 = {float_0: float_0, float_0: float_0, float_0: bytes_0}
            var_0 = module_0.lazyclassproperty(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
