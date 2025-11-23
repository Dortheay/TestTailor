import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'Zp!P\tn|*'
        corrected_command_0 = None
        bytes_0 = b'\xc4q^\x1e\xc8\x804\x9f'
        dict_0 = {corrected_command_0: str_0, bytes_0: str_0}
        bool_0 = True
        list_0 = [bool_0, bytes_0, bytes_0]
        float_0 = 1762.70062
        tuple_0 = (corrected_command_0, bytes_0, float_0)
        bytes_1 = b'\xdf\xc9\ry\xd7'
        rule_0 = module_0.Rule(str_0, str_0, corrected_command_0, dict_0, list_0, tuple_0, bytes_1)
        int_0 = None
        set_0 = {int_0}
        tuple_1 = (set_0,)
        bytes_2 = b'\xf2\xa5\xb1\x8d\xde\x11&b\xb2h'
        int_1 = 2475
        list_1 = [int_1, tuple_1]
        str_1 = 'a<.\tgo<d_.'
        str_2 = '-A'
        bytes_3 = b'\x19\xa6\xe5\xe2\xd3\x17\xac4St'
        command_0 = module_0.Command(str_2, bytes_3)
        command_1 = module_0.Command(command_0, corrected_command_0)
        dict_1 = {}
        str_3 = 'permission denied'
        rule_1 = module_0.Rule(command_1, dict_1, corrected_command_0, rule_0, dict_1, str_2, str_3)
        command_2 = module_0.Command(tuple_1, rule_1)
        var_0 = command_2.__eq__(list_0)
        float_1 = 2107.019495
        list_2 = [set_0]
        corrected_command_1 = module_0.CorrectedCommand(tuple_1, list_1, list_1)
        bytes_4 = b'\xab\xa5z\xff\x01\xc0+!'
        rule_2 = module_0.Rule(list_1, str_1, float_1, list_1, list_2, corrected_command_1, bytes_4)
        str_4 = 'ㅔ'
        dict_2 = {}
        dict_3 = {}
        rule_3 = module_0.Rule(tuple_1, bytes_2, set_0, rule_2, str_4, dict_2, dict_3)
        var_1 = rule_3.__eq__(rule_0)

if __name__ == "__main__":
    unittest.main()
