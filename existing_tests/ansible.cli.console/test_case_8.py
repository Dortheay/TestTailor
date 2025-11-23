import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '\ns@tFT'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        int_0 = -3716
        var_0 = console_c_l_i_0.do_timeout(int_0)

if __name__ == "__main__":
    unittest.main()
