import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            tuple_0 = None
            str_0 = None
            str_1 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_1)
            var_0 = console_c_l_i_0.list_modules()
            var_1 = console_c_l_i_0.do_exit(str_0)
            var_2 = console_c_l_i_0.do_timeout(tuple_0)
            var_3 = console_c_l_i_0.do_verbosity(str_1)
            str_2 = '\ns@tFT'
            console_c_l_i_1 = module_0.ConsoleCLI(str_2)
            console_c_l_i_2 = module_0.ConsoleCLI(console_c_l_i_1)
            var_4 = console_c_l_i_2.list_modules()
            int_0 = -1396
            var_5 = console_c_l_i_2.do_cd(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
