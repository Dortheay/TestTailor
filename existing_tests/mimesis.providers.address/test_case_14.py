import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        address_0 = module_0.Address()
        str_0 = address_0.zip_code()
        str_1 = address_0.federal_subject()
        str_2 = address_0.city()
        str_3 = address_0.prefecture()
        address_1 = module_0.Address()
        str_4 = address_1.calling_code()
        bool_0 = True
        var_0 = address_0.latitude()
        str_5 = address_1.street_number()
        str_6 = address_0.state(bool_0)
        dict_0 = address_0.coordinates(bool_0)
        str_7 = address_0.state()
        dict_1 = address_1.coordinates(bool_0)
        list_0 = [str_6, str_1]
        address_2 = module_0.Address(*list_0)
        str_8 = address_2.address()
        str_9 = address_2.address()
        str_10 = address_0.country(bool_0)

if __name__ == "__main__":
    unittest.main()
