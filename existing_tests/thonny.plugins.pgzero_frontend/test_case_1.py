import unittest
import timeout_decorator
import thonny.plugins.pgzero_frontend as module_0

class Test_Pgzero_frontend_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = module_0.toggle_variable()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
