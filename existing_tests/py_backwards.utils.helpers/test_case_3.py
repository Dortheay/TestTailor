import unittest
import timeout_decorator
import py_backwards.utils.helpers as module_0

class Test_Helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'MH2kW+mE\x0cBoU,jDq?q'
        module_0.warn(str_0)

if __name__ == "__main__":
    unittest.main()
