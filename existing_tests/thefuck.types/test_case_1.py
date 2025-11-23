import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'BUwSN6m457}>:qamj$^U'
            dict_0 = {str_0: str_0, str_0: str_0}
            list_0 = None
            command_0 = module_0.Command(dict_0, list_0)
            int_0 = -1028
            bytes_0 = b'\x04\x94\x1a'
            int_1 = 60
            corrected_command_0 = module_0.CorrectedCommand(int_0, bytes_0, int_1)
            bool_0 = True
            dict_1 = {}
            str_1 = '07g-}&n:vD\r'
            int_2 = -4707
            rule_0 = module_0.Rule(corrected_command_0, bytes_0, list_0, bool_0, dict_1, str_1, int_2)
            var_0 = rule_0.is_match(command_0)
            dict_2 = {}
            var_1 = corrected_command_0.run(dict_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
