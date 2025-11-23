import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '1.2.3'
            str_1 = module_0.bump_version(str_0)
            int_0 = 1
            str_2 = module_0.bump_version(str_0, int_0)
            str_3 = module_0.bump_version(str_0, int_0)
            str_4 = 'A'
            str_5 = module_0.bump_version(str_3, int_0, str_4)
            int_1 = -1920
            str_6 = module_0.bump_version(str_2, int_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
