import unittest
import timeout_decorator
import mimesis.providers.base as module_0

class Test_Base_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        base_provider_0 = module_0.BaseProvider()
        str_0 = base_provider_0.__str__()
        str_1 = base_provider_0.__str__()
        base_data_provider_0 = module_0.BaseDataProvider()
        str_2 = base_data_provider_0.get_current_locale()

if __name__ == "__main__":
    unittest.main()
