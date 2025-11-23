import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = -652.42023
        set_0 = {float_0, float_0}
        console_c_l_i_0 = module_0.ConsoleCLI(set_0)
        var_0 = console_c_l_i_0.list_modules()
        var_1 = console_c_l_i_0.get_names()

if __name__ == "__main__":
    unittest.main()
