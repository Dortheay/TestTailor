import unittest
import timeout_decorator
import mimesis.providers.base as module_0

class Test_Base_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        base_provider_0 = module_0.BaseProvider()
        str_0 = base_provider_0.__str__()

if __name__ == "__main__":
    unittest.main()
