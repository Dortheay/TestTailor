import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'uH=EX?m\x0bZ\x0cwT'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_0.do_timeout(str_0)

if __name__ == "__main__":
    unittest.main()
