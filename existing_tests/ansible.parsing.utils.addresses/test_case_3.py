import unittest
import timeout_decorator
import ansible.parsing.utils.addresses as module_0

class Test_Addresses_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'OVS'
        var_0 = module_0.parse_address(str_0)

if __name__ == "__main__":
    unittest.main()
