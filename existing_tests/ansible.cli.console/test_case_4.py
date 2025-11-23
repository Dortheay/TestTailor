import unittest
import timeout_decorator
import ansible.cli.console as module_0

class Test_Console_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        set_0 = set()
        str_0 = "takes a dictionary and transforms it into a list of dictionaries,\n    with each having a 'key' and 'value' keys that correspond to the keys and values of the original"
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_0.do_forks(set_0)
        str_1 = '+p;I=!&;V6/M4]\x0c4@'
        console_c_l_i_1 = module_0.ConsoleCLI(str_1)
        var_1 = console_c_l_i_1.emptyline()

if __name__ == "__main__":
    unittest.main()
