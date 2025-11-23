import unittest
import timeout_decorator
import flutils.decorators as module_0

class Test_Decorators_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'6\x0e'
            cached_property_0 = module_0.cached_property(bytes_0)
            var_0 = cached_property_0.__get__(bytes_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
