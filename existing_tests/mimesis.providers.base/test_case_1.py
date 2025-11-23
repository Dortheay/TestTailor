import unittest
import timeout_decorator
import mimesis.providers.base as module_0

class Test_Base_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = 505
        base_provider_0 = module_0.BaseProvider(int_0)

if __name__ == "__main__":
    unittest.main()
