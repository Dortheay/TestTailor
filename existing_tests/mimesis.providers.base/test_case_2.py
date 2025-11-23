import unittest
import timeout_decorator
import mimesis.providers.base as module_0

class Test_Base_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        base_provider_0 = module_0.BaseProvider()
        base_provider_0.reseed()

if __name__ == "__main__":
    unittest.main()
