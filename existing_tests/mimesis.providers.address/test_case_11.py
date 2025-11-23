import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        address_0 = module_0.Address()
        str_0 = address_0.street_name()
        str_1 = address_0.street_number()
        var_0 = address_0.longitude()
        str_2 = address_0.calling_code()
        str_3 = address_0.street_suffix()
        str_4 = address_0.street_name()

if __name__ == "__main__":
    unittest.main()
