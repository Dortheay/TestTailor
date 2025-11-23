import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = '\ns@tFT'
            console_c_l_i_0 = module_0.ConsoleCLI(str_0)
            bytes_0 = b'?~wT\xa8\xb8\x1c('
            str_1 = '>3w7AIm,UJx\x0b&T35'
            str_2 = 'F>aG\n#SG?4@+`"'
            console_c_l_i_1 = module_0.ConsoleCLI(str_2)
            var_0 = console_c_l_i_1.complete_cd(console_c_l_i_0, bytes_0, str_1, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
