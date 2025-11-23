import unittest
import timeout_decorator
import flutils.packages as module_0

class Test_Packages_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '1.2.3'
        str_1 = module_0.bump_version(str_0)

if __name__ == "__main__":
    unittest.main()
