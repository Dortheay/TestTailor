import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xbe\xf4\xe2'
            console_c_l_i_0 = module_0.ConsoleCLI(bytes_0)
            var_0 = console_c_l_i_0.cmdloop()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
