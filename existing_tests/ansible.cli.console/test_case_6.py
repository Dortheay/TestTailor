import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'm\t '
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        str_1 = 'CX'
        str_2 = 's,M+r&_'
        console_c_l_i_1 = module_0.ConsoleCLI(str_2)
        var_0 = console_c_l_i_1.do_check(str_1)
        bytes_0 = b'\x85Mj\xb0\xb4\xac'
        int_0 = -598
        str_3 = '1o'
        var_1 = console_c_l_i_0.complete_cd(bytes_0, str_0, int_0, str_3)
        float_0 = 2174.44595
        tuple_0 = ()
        var_2 = console_c_l_i_1.do_become_method(tuple_0)
        console_c_l_i_2 = module_0.ConsoleCLI(float_0)

if __name__ == "__main__":
    unittest.main()
