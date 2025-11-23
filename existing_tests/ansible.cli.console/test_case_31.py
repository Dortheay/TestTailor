import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
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
            console_c_l_i_2 = module_0.ConsoleCLI(set_0)
            var_2 = console_c_l_i_1.do_timeout(set_0)
            var_3 = console_c_l_i_0.do_verbosity(str_1)
            var_4 = console_c_l_i_2.emptyline()
            int_0 = -2232
            var_5 = console_c_l_i_0.do_become_method(int_0)
            int_1 = -945
            var_6 = console_c_l_i_2.do_forks(int_1)
            var_7 = console_c_l_i_0.do_diff(int_1)
            var_8 = console_c_l_i_2.init_parser()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
