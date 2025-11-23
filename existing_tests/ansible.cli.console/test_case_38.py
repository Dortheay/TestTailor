import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_28(self):
        try:
            str_0 = '>@jM&%-U|EcNo.'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            str_1 = '\ns@tFT'
            set_0 = None
            str_2 = 'Wl:}HW\\gD0'
            console_c_l_i_1 = module_0.ConsoleCLI(str_2)
            var_0 = console_c_l_i_1.do_check(set_0)
            console_c_l_i_2 = module_0.ConsoleCLI(str_1)
            var_1 = console_c_l_i_0.do_timeout(console_c_l_i_2)
            str_3 = '>3w7AIm,UJx\x0b&T35'
            var_2 = console_c_l_i_2.init_parser()
            var_3 = console_c_l_i_2.do_shell(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
