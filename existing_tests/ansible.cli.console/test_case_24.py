import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            tuple_0 = None
            str_0 = None
            str_1 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.do_exit(str_0)
            var_1 = console_c_l_i_0.do_timeout(tuple_0)
            float_0 = 1208.0
            console_c_l_i_1 = module_0.ConsoleCLI(float_0)
            var_2 = console_c_l_i_0.do_verbosity(str_1)
            str_2 = '\ns@tFT'
            console_c_l_i_2 = module_0.ConsoleCLI(str_2)
            str_3 = 'jIJ|'
            var_3 = console_c_l_i_2.do_become_method(str_3)
            bool_0 = False
            var_4 = console_c_l_i_2.do_forks(bool_0)
            str_4 = '5]odUQ|"Jw,v'
            var_5 = console_c_l_i_2.do_diff(console_c_l_i_2)
            var_6 = console_c_l_i_2.init_parser()
            var_7 = console_c_l_i_2.do_shell(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
