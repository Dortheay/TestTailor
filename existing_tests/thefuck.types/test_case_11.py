import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bytes_0 = b"\x1c\xad\xc9g~.\x08pa\x8as'\x14\xa6|Z"
        int_0 = -191
        float_0 = 189.0
        set_0 = {int_0, int_0}
        corrected_command_0 = module_0.CorrectedCommand(int_0, float_0, set_0)
        var_0 = corrected_command_0.__eq__(bytes_0)

if __name__ == "__main__":
    unittest.main()
