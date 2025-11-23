import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            address_0 = module_0.Address()
            str_0 = address_0.state()
            str_1 = address_0.postal_code()
            str_2 = address_0.address()
            str_3 = None
            dict_0 = {str_3: str_3}
            bool_0 = False
            str_4 = address_0.continent()
            str_5 = address_0.street_suffix()
            str_6 = address_0.address()
            str_7 = address_0.country(bool_0)
            var_0 = address_0.longitude()
            address_1 = module_0.Address(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
