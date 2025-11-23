import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        address_0 = module_0.Address()
        str_0 = address_0.postal_code()
        list_0 = [address_0]
        dict_0 = {}
        str_1 = address_0.region(*list_0, **dict_0)
        str_2 = address_0.zip_code()

if __name__ == "__main__":
    unittest.main()
