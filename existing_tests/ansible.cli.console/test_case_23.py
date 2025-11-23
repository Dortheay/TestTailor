import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = '\ns@tFT'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            bytes_0 = b'?~wT\xa8\xb8\x1c('
            var_0 = console_c_l_i_0.init_parser()
            console_c_l_i_1 = module_0.ConsoleCLI(console_c_l_i_0)
            set_0 = None
            var_1 = console_c_l_i_1.do_timeout(set_0)
            console_c_l_i_2 = module_0.ConsoleCLI(console_c_l_i_1)
            int_0 = None
            var_2 = console_c_l_i_2.do_diff(int_0)
            var_3 = console_c_l_i_2.emptyline()
            var_4 = console_c_l_i_1.post_process_args(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
