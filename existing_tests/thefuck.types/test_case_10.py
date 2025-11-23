import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = ''
        float_0 = 1003.0
        bool_0 = False
        command_0 = module_0.Command(str_0, bool_0)
        corrected_command_0 = module_0.CorrectedCommand(str_0, float_0, command_0)

if __name__ == "__main__":
    unittest.main()
