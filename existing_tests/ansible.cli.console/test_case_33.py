import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            tuple_0 = None
            str_0 = None
            str_1 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.do_exit(str_0)
            str_2 = 'groups'
            set_0 = {str_2, str_2, str_2, str_2}
            console_c_l_i_1 = module_0.ConsoleCLI(set_0)
            var_1 = console_c_l_i_1.do_verbosity(tuple_0)
            str_3 = '-yNf1)Ts:'
            console_c_l_i_2 = module_0.ConsoleCLI(str_3)
            bool_0 = False
            var_2 = console_c_l_i_2.do_forks(bool_0)
            str_4 = '>3w7AIm,UJx\x0b&T35'
            var_3 = console_c_l_i_2.init_parser()
            var_4 = console_c_l_i_2.do_shell(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
