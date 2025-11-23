import unittest
import timeout_decorator
import ansible.parsing.utils.addresses as module_0

class Test_Addresses_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = ''
            var_0 = module_0.parse_address(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
