import unittest
import timeout_decorator
import mimesis.providers.base as module_0

class Test_Base_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        base_data_provider_0 = module_0.BaseDataProvider()
        str_0 = base_data_provider_0.__str__()

if __name__ == "__main__":
    unittest.main()
