import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'L!fE\r/<\\KXh'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_0.run()

if __name__ == "__main__":
    unittest.main()
