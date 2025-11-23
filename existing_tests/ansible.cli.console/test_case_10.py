import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '\ns@tFT'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            int_0 = -3716
            var_0 = console_c_l_i_0.do_timeout(int_0)
            set_0 = {var_0}
            var_1 = console_c_l_i_0.post_process_args(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
