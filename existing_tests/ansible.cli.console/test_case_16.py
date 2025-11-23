import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = -1391
            str_0 = 'm\t '
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            float_0 = -1300.0
            tuple_0 = ()
            var_0 = console_c_l_i_0.do_become_method(tuple_0)
            console_c_l_i_1 = module_0.ConsoleCLI(float_0)
            var_1 = console_c_l_i_1.do_list(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
