import unittest
import timeout_decorator
import mimesis.providers.base as module_0

class Test_Base_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 49151
        base_provider_0 = module_0.BaseProvider()
        str_0 = base_provider_0.__str__()
        base_provider_1 = module_0.BaseProvider(int_0)
        base_provider_1.reseed()

if __name__ == "__main__":
    unittest.main()
