import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            bytes_0 = b'\x06\xa4V'
            int_0 = 2359
            console_c_l_i_0 = module_0.ConsoleCLI(int_0)
            var_0 = console_c_l_i_0.helpdefault(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
