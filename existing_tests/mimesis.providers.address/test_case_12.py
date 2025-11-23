import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        address_0 = module_0.Address()
        bool_0 = True
        dict_0 = address_0.coordinates(bool_0)
        str_0 = address_0.address()

if __name__ == "__main__":
    unittest.main()
