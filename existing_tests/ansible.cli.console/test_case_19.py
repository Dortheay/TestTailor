import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 257
            str_0 = 'n17tZ@f}G83Aw<).i1*'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            var_0 = console_c_l_i_0.do_remote_user(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
