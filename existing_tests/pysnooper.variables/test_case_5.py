import unittest
import timeout_decorator
import pysnooper.variables as module_0

class Test_Variables_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'mock_source'
        indices_0 = module_0.Indices(str_0)
        int_0 = 15
        int_1 = 5
        var_0 = slice(int_0, int_1)
        var_1 = indices_0[var_0]

if __name__ == "__main__":
    unittest.main()
