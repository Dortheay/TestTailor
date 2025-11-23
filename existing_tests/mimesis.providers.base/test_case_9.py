import unittest
import timeout_decorator
import mimesis.providers.base as module_0
import builtins as module_1

class Test_Base_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '7j'
            base_data_provider_0 = module_0.BaseDataProvider(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
