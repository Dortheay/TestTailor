import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        internet_0 = module_0.Internet()
        bool_0 = True
        str_0 = internet_0.ip_v4(bool_0)
        str_1 = internet_0.network_protocol()

if __name__ == "__main__":
    unittest.main()
