import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            version_info_0 = module_0._VersionInfo()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
