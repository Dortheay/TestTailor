import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 2648
            set_0 = {int_0, int_0}
            str_0 = 'E\nx'
            str_1 = 'sB&0*A<hS#hg.4H0@[T'
            dict_0 = {str_1: str_1, str_0: str_0, str_1: str_1}
            float_0 = 3180.879873
            str_2 = '0=7BU'
            dict_1 = {float_0: str_0, str_1: str_1, str_2: str_1}
            float_1 = -674.31
            corrected_command_0 = module_0.CorrectedCommand(dict_1, dict_0, float_1)
            command_0 = module_0.Command(str_2, corrected_command_0)
            var_0 = command_0.__eq__(command_0)
            str_3 = 'c~&=\rbZcD=\x0b`;*W)Q1'
            list_0 = []
            str_4 = 'PA< mK\x0c9bJ'
            set_1 = set()
            rule_0 = module_0.Rule(dict_0, str_3, list_0, corrected_command_0, str_4, set_1, set_0)
            var_1 = rule_0.__repr__()
            bytes_0 = b"'\xc4-\xd1\x96/{\x97\x15"
            rule_1 = module_0.Rule(dict_0, int_0, float_0, dict_0, command_0, str_1, bytes_0)
            var_2 = command_0.__repr__()
            var_3 = rule_1.__eq__(set_0)
            dict_2 = {}
            var_4 = corrected_command_0.__eq__(dict_1)
            bool_0 = False
            bytes_1 = b'P\xe9\xdb\x0ew\xafo\x17\x8757I4\x08\xb5'
            set_2 = {bytes_1}
            bytes_2 = b'+\xe8\xc7\xed\xed\x99^\xf6\x1e\xfe\x95'
            corrected_command_1 = module_0.CorrectedCommand(bytes_2, dict_2, bool_0)
            var_5 = rule_1.get_corrected_commands(bool_0)
            complex_0 = None
            var_6 = rule_1.__repr__()
            bytes_3 = b'\xf6\xa5E}cILF\xc4\xf0|\xdb\xf1\xd9\x88\xec\xd7\xe2'
            tuple_0 = (complex_0, dict_2, bytes_3, dict_2)
            var_7 = command_0.__eq__(tuple_0)
            var_8 = corrected_command_1.run(set_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
