import unittest
import timeout_decorator
import flutils.decorators as module_0

class Test_Decorators_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = None
        bytes_1 = b'6\x0e'
        cached_property_0 = module_0.cached_property(bytes_1)
        var_0 = cached_property_0.__get__(bytes_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
