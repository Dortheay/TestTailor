import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        address_0 = module_0.Address()
        bool_0 = True
        dict_0 = address_0.coordinates(bool_0)

if __name__ == "__main__":
    unittest.main()
