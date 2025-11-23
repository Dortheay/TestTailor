import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        address_0 = module_0.Address()
        str_0 = address_0.address()

if __name__ == "__main__":
    unittest.main()
