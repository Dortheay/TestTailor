import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'm\t '
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_0.init_parser()
        var_1 = console_c_l_i_0.do_check(str_0)
        float_0 = 2174.44595
        tuple_0 = ()
        var_2 = console_c_l_i_0.do_become_method(tuple_0)
        console_c_l_i_1 = module_0.ConsoleCLI(float_0)

if __name__ == "__main__":
    unittest.main()
