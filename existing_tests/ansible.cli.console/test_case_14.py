import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '\ns@tFT'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            var_0 = console_c_l_i_0.do_forks(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
