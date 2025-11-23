import unittest
import timeout_decorator
import thonny.jedi_utils as module_0

class Test_Jedi_utils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -875
            var_0 = module_0.parse_source(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
