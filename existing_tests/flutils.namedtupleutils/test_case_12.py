import unittest
import timeout_decorator
import collections.abc as module_0
import flutils.namedtupleutils as module_1

class Test_Namedtupleutils_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'raw_utf8_escape'
            var_0 = module_1.to_namedtuple(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
