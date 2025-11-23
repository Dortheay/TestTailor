import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'action'
            str_1 = 'args'
            str_2 = 'copy'
            str_3 = 'src'
            str_4 = 'file_a'
            str_5 = {str_3: str_4, str_1: str_3}
            str_6 = {str_0: str_2, str_1: str_5}
            module_args_parser_0 = module_0.ModuleArgsParser(str_6)
            var_0 = module_args_parser_0.parse()
            module_args_parser_1 = module_0.ModuleArgsParser(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
