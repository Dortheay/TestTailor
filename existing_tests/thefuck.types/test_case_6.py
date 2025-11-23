import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -2950
        list_0 = [int_0, int_0, int_0, int_0]
        int_1 = 4000
        str_0 = 'no such file or directory'
        str_1 = '.V'
        str_2 = 'YB|fh,cr\t'
        dict_0 = {str_1: list_0, str_2: str_1}
        command_0 = module_0.Command(dict_0, list_0)
        var_0 = command_0.__eq__(str_0)
        tuple_0 = (int_1,)
        corrected_command_0 = module_0.CorrectedCommand(int_0, list_0, tuple_0)
        str_3 = '`|>7s;;y|-EBP4'
        set_0 = {tuple_0}
        command_1 = module_0.Command(str_3, set_0)

if __name__ == "__main__":
    unittest.main()
