import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'BUwSN6m457}>:qamj$^U'
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = None
        command_0 = module_0.Command(str_0, dict_0)
        bytes_0 = b'\x04\x94\x1a'
        int_0 = 60
        corrected_command_0 = module_0.CorrectedCommand(int_0, bytes_0, int_0)
        var_0 = corrected_command_0.__hash__()
        bool_0 = True
        int_1 = -4742
        rule_0 = module_0.Rule(corrected_command_0, bytes_0, list_0, bool_0, dict_0, str_0, int_1)
        var_1 = rule_0.is_match(command_0)

if __name__ == "__main__":
    unittest.main()
