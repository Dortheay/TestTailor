import unittest
import timeout_decorator
import pysnooper.variables as module_0

class Test_Variables_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'mlr9JL'
            attrs_0 = module_0.Attrs(str_0)
            bytes_0 = b'\x0c\x018>N\xc6\x01\x08\xf7\xc9b\xf8'
            base_variable_0 = module_0.BaseVariable(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
