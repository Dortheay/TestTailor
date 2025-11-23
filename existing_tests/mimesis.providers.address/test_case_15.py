import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            address_0 = module_0.Address()
            str_0 = address_0.street_name()
            str_1 = address_0.street_suffix()
            address_1 = module_0.Address()
            str_2 = address_1.federal_subject()
            str_3 = 'Tonar'
            dict_0 = {str_3: str_2}
            str_4 = address_1.province(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
