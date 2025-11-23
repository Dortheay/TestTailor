import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            address_0 = module_0.Address()
            str_0 = address_0.prefecture()
            address_1 = module_0.Address()
            str_1 = address_1.address()
            bool_0 = True
            str_2 = address_1.continent(bool_0)
            address_2 = module_0.Address()
            str_3 = address_2.street_name()
            bool_1 = True
            str_4 = address_1.city()
            dict_0 = {}
            address_3 = module_0.Address()
            str_5 = address_3.province(**dict_0)
            list_0 = [address_1]
            str_6 = address_1.prefecture(*list_0)
            var_0 = address_0.longitude(bool_1)
            str_7 = address_0.street_number()
            str_8 = address_1.calling_code()
            str_9 = address_0.city()
            str_10 = address_1.city()
            str_11 = address_1.province()
            int_0 = -1141
            str_12 = address_1.street_number(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
