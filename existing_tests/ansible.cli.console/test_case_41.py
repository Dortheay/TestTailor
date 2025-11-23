import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            tuple_0 = None
            str_0 = None
            str_1 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.list_modules()
            var_1 = console_c_l_i_0.do_exit(str_0)
            str_2 = 'groups'
            var_2 = console_c_l_i_0.do_timeout(tuple_0)
            set_0 = {str_2, str_2, str_2, str_2}
            console_c_l_i_1 = module_0.ConsoleCLI(set_0)
            float_0 = -3752.4
            console_c_l_i_2 = module_0.ConsoleCLI(float_0)
            console_c_l_i_3 = module_0.ConsoleCLI(set_0)
            var_3 = console_c_l_i_1.emptyline()
            bytes_0 = None
            dict_0 = {bytes_0: str_1, console_c_l_i_3: var_1, bytes_0: set_0, str_0: var_2}
            console_c_l_i_4 = module_0.ConsoleCLI(dict_0)
            bool_0 = False
            var_4 = console_c_l_i_0.do_become_method(bool_0)
            int_0 = None
            var_5 = console_c_l_i_4.do_forks(int_0)
            str_3 = 'groups'
            var_6 = console_c_l_i_4.do_list(str_3)
            var_7 = console_c_l_i_1.do_diff(float_0)
            str_4 = "'"
            var_8 = console_c_l_i_1.do_shell(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
