import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '1.2.3'
        int_0 = 1
        str_1 = module_0.bump_version(str_0, int_0)
        str_2 = module_0.bump_version(str_1)

if __name__ == "__main__":
    unittest.main()
