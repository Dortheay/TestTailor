import unittest
import timeout_decorator
import collections.abc as module_0
import flutils.namedtupleutils as module_1

class Test_Namedtupleutils_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            mapping_0 = module_0.Mapping()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
