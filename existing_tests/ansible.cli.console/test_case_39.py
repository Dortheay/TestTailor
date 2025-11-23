import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            tuple_0 = None
            str_0 = None
            str_1 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.do_exit(str_0)
            int_0 = -1396
            var_1 = console_c_l_i_0.do_timeout(int_0)
            var_2 = console_c_l_i_0.do_timeout(tuple_0)
            console_c_l_i_1 = module_0.ConsoleCLI(int_0)
            str_2 = 'H^FOW#35uS;\'"iY^_#JX'
            var_3 = console_c_l_i_0.do_timeout(str_2)
            float_0 = 1896.64373
            var_4 = console_c_l_i_1.do_verbosity(float_0)
            var_5 = console_c_l_i_1.emptyline()
            float_1 = 0.2
            console_c_l_i_2 = module_0.ConsoleCLI(float_1)
            bool_0 = True
            list_0 = [bool_0, str_1, console_c_l_i_1]
            var_6 = console_c_l_i_1.do_become_method(list_0)
            var_7 = console_c_l_i_0.do_forks(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
