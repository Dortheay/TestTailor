import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = -1
            str_0 = 'b'
            str_1 = '1.2.4b0'
            str_2 = module_0.bump_version(str_1, int_0, str_0)
            str_3 = '?'
            str_4 = module_0.bump_version(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
