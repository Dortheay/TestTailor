import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            tuple_0 = None
            str_0 = None
            str_1 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.do_exit(str_0)
            str_2 = 'groups'
            var_1 = console_c_l_i_0.do_timeout(tuple_0)
            set_0 = {str_2, str_2, str_2, str_2}
            console_c_l_i_1 = module_0.ConsoleCLI(set_0)
            var_2 = console_c_l_i_1.do_verbosity(tuple_0)
            var_3 = console_c_l_i_1.emptyline()
            str_3 = '\ns@tFT'
            console_c_l_i_2 = module_0.ConsoleCLI(str_3)
            var_4 = console_c_l_i_0.init_parser()
            bool_0 = False
            var_5 = console_c_l_i_2.do_forks(bool_0)
            str_4 = 'BMz@g]V8p14b'
            var_6 = console_c_l_i_2.module_args(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
