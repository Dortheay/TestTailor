import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            list_0 = []
            address_0 = module_0.Address(*list_0)
            str_0 = address_0.country_code()
            str_1 = address_0.federal_subject(**dict_0)
            address_1 = module_0.Address()
            str_2 = address_1.prefecture(**dict_0)
            int_0 = 3577
            str_3 = address_1.street_number(int_0)
            str_4 = address_1.prefecture()
            list_1 = [address_1, str_2, dict_0, str_2]
            str_5 = address_1.province(*list_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
