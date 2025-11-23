import unittest
import timeout_decorator
import mimesis.providers.generic as module_0

class Test_Generic_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = " q&'XBr2&@"
            generic_0 = module_0.Generic()
            any_0 = generic_0.__getattr__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
