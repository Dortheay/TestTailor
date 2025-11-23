import unittest
import timeout_decorator
import pysnooper.variables as module_0

class Test_Variables_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'mock_surce'
        indices_0 = module_0.Indices(str_0)
        int_0 = 1
        int_1 = 5
        var_0 = slice(int_0, int_1)
        var_1 = indices_0[var_0]
        set_0 = {indices_0, var_1}
        var_2 = slice(set_0)

if __name__ == "__main__":
    unittest.main()
