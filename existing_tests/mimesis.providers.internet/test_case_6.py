import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        internet_0 = module_0.Internet()
        str_0 = internet_0.network_protocol()

if __name__ == "__main__":
    unittest.main()
