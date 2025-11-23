import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            float_0 = -376.4852
            console_c_l_i_0 = module_0.ConsoleCLI(float_0)
            str_0 = "]'AclQRU46F>Q5'5"
            var_0 = console_c_l_i_0.do_become_method(str_0)
            var_1 = console_c_l_i_0.get_names()
            str_1 = '0'
            var_2 = console_c_l_i_0.do_cd(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
