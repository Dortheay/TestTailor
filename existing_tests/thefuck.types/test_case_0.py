import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            bool_0 = False
            bytes_0 = b'P\xe9\xdb\x0ew\xafo\x17\x8757I4\x08\xb5'
            set_0 = {bytes_0}
            bytes_1 = b'+\xe8\xc7\xed\xed\x99^\xf6\x1e\xfe\x95'
            corrected_command_0 = module_0.CorrectedCommand(bytes_1, dict_0, bool_0)
            var_0 = corrected_command_0.run(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
