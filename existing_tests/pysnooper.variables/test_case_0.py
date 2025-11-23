import unittest
import timeout_decorator
import pysnooper.variables as module_0

class Test_Variables_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = "\\tA<\x0b4U<7/'`'}5:o"
            base_variable_0 = module_0.BaseVariable(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
