import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'\xf8\xb1\x96\x85\xfb&U\x07O\xc2\xb83N6Ec\x0c\x96'
        console_c_l_i_0 = module_0.ConsoleCLI(bytes_0)
        var_0 = console_c_l_i_0.list_modules()

if __name__ == "__main__":
    unittest.main()
