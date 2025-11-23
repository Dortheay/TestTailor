import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            float_0 = 4271.488
            list_0 = [dict_0, dict_0]
            bytes_0 = b'(\xed'
            list_1 = [float_0, dict_0, dict_0]
            str_0 = ''
            str_1 = 'X'
            bool_0 = False
            float_1 = 0.85
            dict_1 = {}
            corrected_command_0 = module_0.CorrectedCommand(list_0, float_1, dict_1)
            rule_0 = module_0.Rule(dict_0, str_1, list_0, bool_0, bool_0, bytes_0, corrected_command_0)
            var_0 = rule_0.__eq__(dict_0)
            bool_1 = False
            corrected_command_1 = module_0.CorrectedCommand(list_1, str_0, bool_1)
            var_1 = corrected_command_1.__eq__(bytes_0)
            bytes_1 = b'P\xe9\xdb\x0ew\xafo\x17\x8757I4\x08\xb5'
            set_0 = {bytes_1}
            corrected_command_2 = module_0.CorrectedCommand(bytes_0, var_1, str_0)
            var_2 = corrected_command_2.run(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
