import unittest
import timeout_decorator
import pysnooper.variables as module_0

class Test_Variables_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'\x93\xc5o~\xe4p\xbd\x8b;x7\xc3\xa6\xf7\xa2'
            attrs_0 = module_0.Attrs(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
