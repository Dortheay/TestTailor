import unittest
import timeout_decorator
import collections.abc as module_0
import flutils.namedtupleutils as module_1

class Test_Namedtupleutils_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = None
            var_1 = module_1.to_namedtuple(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
