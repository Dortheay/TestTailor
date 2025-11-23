import unittest
import timeout_decorator
import pysnooper.variables as module_0

class Test_Variables_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'mock_source'
            indices_0 = module_0.Indices(str_0)
            int_0 = 5
            var_0 = slice(int_0, int_0)
            var_1 = indices_0[var_0]
            str_1 = 'XhD{'
            var_2 = indices_0.__getitem__(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
