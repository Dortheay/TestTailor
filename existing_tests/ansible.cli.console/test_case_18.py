import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            tuple_0 = None
            str_0 = None
            str_1 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.do_exit(str_0)
            str_2 = 'groups'
            var_1 = console_c_l_i_0.do_timeout(tuple_0)
            set_0 = {str_2, str_2, str_2, str_2}
            float_0 = -1108.72
            console_c_l_i_1 = module_0.ConsoleCLI(float_0)
            str_3 = ''
            var_2 = console_c_l_i_1.do_become(str_3)
            console_c_l_i_2 = module_0.ConsoleCLI(set_0)
            var_3 = console_c_l_i_1.do_timeout(set_0)
            var_4 = console_c_l_i_0.do_verbosity(str_1)
            var_5 = console_c_l_i_2.emptyline()
            str_4 = '\ns@tFT'
            var_6 = console_c_l_i_0.emptyline()
            console_c_l_i_3 = module_0.ConsoleCLI(str_4)
            str_5 = 'jIJ|'
            var_7 = console_c_l_i_3.do_become_method(str_5)
            bool_0 = False
            var_8 = console_c_l_i_3.do_forks(bool_0)
            str_6 = '5odUQ|"Jw,xv'
            var_9 = console_c_l_i_3.do_diff(console_c_l_i_3)
            var_10 = console_c_l_i_3.init_parser()
            var_11 = console_c_l_i_3.do_shell(str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
