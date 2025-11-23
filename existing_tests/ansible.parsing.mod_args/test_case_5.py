import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'ction'
            str_1 = 'i'
            str_2 = {str_0: str_1}
            var_0 = {}
            module_args_parser_0 = module_0.ModuleArgsParser(str_2)
            module_args_parser_1 = module_0.ModuleArgsParser(var_0)
            var_1 = module_args_parser_0.parse()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
