import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = None
            str_1 = module_0.bump_version(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
