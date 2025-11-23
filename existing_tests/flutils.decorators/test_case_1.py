import unittest
import timeout_decorator
import flutils.decorators as module_0

class Test_Decorators_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = -28.936496
        cached_property_0 = module_0.cached_property(float_0)

if __name__ == "__main__":
    unittest.main()
