import unittest
import timeout_decorator
import thefuck.types as module_0

class Test_Types_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            var_0 = None
            var_1 = lambda command, script: var_0
            str_0 = 'test_script'
            str_1 = 'test_output'
            command_0 = module_0.Command(str_0, str_1)
            str_2 = 'corrected_script1'
            str_3 = 'corrected_script2'
            str_4 = [str_2, str_3]
            var_2 = lambda command: str_4
            str_5 = 'test_rule'
            bool_0 = True
            var_3 = lambda command: bool_0
            int_0 = 10
            rule_0 = module_0.Rule(str_5, var_3, var_2, bool_0, var_1, int_0, bool_0)
            var_4 = rule_0.get_corrected_commands(command_0)
            var_5 = list(var_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
