import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = '>@jM&%-U|EcNo.'
            str_1 = 'groups'
            set_0 = {str_1, str_1, str_1, str_1}
            float_0 = -1108.72
            console_c_l_i_0 = module_0.ConsoleCLI(float_0)
            console_c_l_i_1 = module_0.ConsoleCLI(set_0)
            var_0 = console_c_l_i_0.do_timeout(set_0)
            var_1 = console_c_l_i_1.do_verbosity(str_0)
            var_2 = console_c_l_i_1.emptyline()
            str_2 = '\ns@tFT'
            var_3 = console_c_l_i_1.emptyline()
            console_c_l_i_2 = module_0.ConsoleCLI(str_2)
            str_3 = 'jIJ|'
            var_4 = console_c_l_i_2.do_become_method(str_3)
            bool_0 = True
            var_5 = console_c_l_i_2.do_forks(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
