import unittest
import timeout_decorator
import mimesis.providers.address as module_0

class Test_Address_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        address_0 = module_0.Address()

if __name__ == "__main__":
    unittest.main()
