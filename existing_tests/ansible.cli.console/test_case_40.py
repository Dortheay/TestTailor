import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            tuple_0 = None
            str_0 = '"^'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            var_0 = console_c_l_i_0.do_cd(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
