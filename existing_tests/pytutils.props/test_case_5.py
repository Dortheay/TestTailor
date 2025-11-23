import unittest
import timeout_decorator
import pytutils.props as module_0

class Test_Props_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = None
        setterproperty_0 = module_0.setterproperty(str_0)

if __name__ == "__main__":
    unittest.main()
