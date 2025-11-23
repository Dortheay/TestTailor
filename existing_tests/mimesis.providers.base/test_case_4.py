import unittest
import timeout_decorator
import mimesis.providers.base as module_0

class Test_Base_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        base_data_provider_0 = module_0.BaseDataProvider()

if __name__ == "__main__":
    unittest.main()
