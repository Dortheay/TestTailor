import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            bool_0 = True
            str_0 = ',NIs?9#-ARRQ(qMV'
            set_0 = {bool_0, bool_0, bool_0, bool_0}
            console_c_l_i_0 = module_0.ConsoleCLI(set_0)
            var_0 = console_c_l_i_0.default(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
