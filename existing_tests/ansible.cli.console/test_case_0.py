import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = -3306
        console_c_l_i_0 = module_0.ConsoleCLI(int_0)

if __name__ == "__main__":
    unittest.main()
