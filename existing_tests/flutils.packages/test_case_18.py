import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '1.2.3'
        str_1 = module_0.bump_version(str_0)
        int_0 = 1
        str_2 = module_0.bump_version(str_0, int_0)
        str_3 = module_0.bump_version(str_0, int_0)
        str_4 = 'A'
        str_5 = module_0.bump_version(str_3, int_0, str_4)
        str_6 = module_0.bump_version(str_5, int_0)

if __name__ == "__main__":
    unittest.main()
