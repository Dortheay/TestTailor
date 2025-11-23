import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            tuple_0 = ()
            str_0 = '=CoW\';\x0cv\rn"'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            var_0 = console_c_l_i_0.get_names()
            var_1 = console_c_l_i_0.do_become_user(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
