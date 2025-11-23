import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = 'l2`Lko'
            list_0 = [str_0, str_0, str_0]
            console_c_l_i_0 = module_0.ConsoleCLI(list_0)
            var_0 = console_c_l_i_0.get_names()
            var_1 = console_c_l_i_0.module_args(console_c_l_i_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
