import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        address_0 = module_0.Address()
        str_0 = address_0.street_number()

if __name__ == "__main__":
    unittest.main()
