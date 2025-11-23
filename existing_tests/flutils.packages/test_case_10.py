import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 1
            str_0 = '1.2.4a1'
            str_1 = 'b'
            str_2 = module_0.bump_version(str_0)
            str_3 = '1.24b0'
            str_4 = module_0.bump_version(str_3, int_0, str_1)
            version_part_0 = module_0._VersionPart()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
