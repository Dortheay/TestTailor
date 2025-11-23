import unittest
import timeout_decorator
import pytutils.excs as module_0

class Test_Excs_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.ok()

if __name__ == "__main__":
    unittest.main()
