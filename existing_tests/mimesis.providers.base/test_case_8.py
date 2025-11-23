import unittest
import timeout_decorator
import mimesis.providers.base as module_0
import builtins as module_1

class Test_Base_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            base_provider_0 = module_0.BaseProvider()
            str_0 = base_provider_0.__str__()
            str_1 = None
            str_2 = base_provider_0.__str__()
            base_data_provider_0 = module_0.BaseDataProvider(str_1, str_1)
            list_0 = [str_1]
            str_3 = base_data_provider_0.get_current_locale()
            bytearray_0 = module_1.bytearray(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
