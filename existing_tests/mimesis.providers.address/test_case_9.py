import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        address_0 = module_0.Address()
        str_0 = address_0.zip_code()
        str_1 = address_0.address()
        str_2 = address_0.address()
        str_3 = address_0.country()

if __name__ == "__main__":
    unittest.main()
