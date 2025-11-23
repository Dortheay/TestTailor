import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = True
        str_0 = "lh\n'WhmXBwV"
        str_1 = 'r9j{V'
        dict_0 = {str_0: bool_0, str_1: bool_0}
        set_0 = set()
        bytes_0 = b'\xc4\xf8\xdb\xf1\x82\xf8\x86m\x95\xf9<\xa8\xb6\xbf\xffy81\xc4`'
        list_0 = [bool_0, set_0, bool_0, str_0]
        bytes_1 = b'\x01\r/\x98\xbb\xb8}\xc1g\xe5\xd1ESR\x1f]\x0e\xd4\x10['
        rule_0 = module_0.Rule(bool_0, dict_0, set_0, bytes_0, bytes_0, list_0, bytes_1)
        dict_1 = {str_0: rule_0, str_1: set_0}
        str_2 = 'hraC?kSn8Us'
        float_0 = -964.446648
        command_0 = module_0.Command(float_0, dict_0)
        str_3 = '.git'
        rule_1 = module_0.Rule(bool_0, dict_1, str_2, command_0, rule_0, str_3, bytes_1)
        var_0 = rule_1.__repr__()

if __name__ == "__main__":
    unittest.main()
