import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        address_0 = module_0.Address()
        bool_0 = True
        var_0 = address_0.latitude()
        dict_0 = address_0.coordinates(bool_0)
        str_0 = address_0.city()
        str_1 = address_0.address()
        bool_1 = True
        str_2 = address_0.country(bool_1)

if __name__ == "__main__":
    unittest.main()
