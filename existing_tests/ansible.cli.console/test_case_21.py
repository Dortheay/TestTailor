import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            bool_0 = True
            int_0 = 743
            set_0 = {bool_0, bool_0, bool_0, int_0}
            console_c_l_i_0 = module_0.ConsoleCLI(bool_0)
            var_0 = console_c_l_i_0.do_become_user(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
