import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 1
        str_0 = '1.2.4a0'
        str_1 = '1.2.4a1'
        str_2 = module_0.bump_version(str_1)
        str_3 = module_0.bump_version(str_0, int_0)
        str_4 = module_0.bump_version(str_0, int_0)

if __name__ == "__main__":
    unittest.main()
