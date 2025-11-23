import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = True
            console_c_l_i_0 = module_0.ConsoleCLI(bool_0)
            var_0 = console_c_l_i_0.list_modules()
            var_1 = console_c_l_i_0.do_cd(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
