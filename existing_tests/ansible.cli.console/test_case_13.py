import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = True
            console_c_l_i_0 = module_0.ConsoleCLI(bool_0)
            var_0 = console_c_l_i_0.do_become_method(console_c_l_i_0)
            var_1 = console_c_l_i_0.get_names()
            var_2 = console_c_l_i_0.do_shell(console_c_l_i_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
