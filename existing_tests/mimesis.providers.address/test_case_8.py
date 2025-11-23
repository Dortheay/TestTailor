import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        address_0 = module_0.Address()
        str_0 = address_0.zip_code()
        str_1 = address_0.city()
        str_2 = address_0.prefecture()
        address_1 = module_0.Address()
        str_3 = address_1.calling_code()
        var_0 = address_0.latitude()
        str_4 = address_1.address()

if __name__ == "__main__":
    unittest.main()
