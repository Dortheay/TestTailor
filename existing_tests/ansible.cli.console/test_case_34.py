import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            str_0 = ':fP?A@%'
            int_0 = -3306
            console_c_l_i_0 = module_0.ConsoleCLI(int_0)
            var_0 = console_c_l_i_0.do_verbosity(str_0)
            bool_0 = False
            console_c_l_i_1 = module_0.ConsoleCLI(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
