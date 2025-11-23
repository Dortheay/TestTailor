import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'action'
        str_1 = 'module'
        str_2 = 'src'
        str_3 = 'dest'
        str_4 = 'copy'
        str_5 = 'a'
        str_6 = 'b'
        str_7 = {str_1: str_4, str_2: str_5, str_3: str_6}
        str_8 = {str_0: str_7}
        module_args_parser_0 = module_0.ModuleArgsParser(str_8)
        str_9 = 'g}^Y&oMNOI.Ua+s.'
        var_0 = module_args_parser_0.parse(str_9)
        var_1 = module_args_parser_0.parse()

if __name__ == "__main__":
    unittest.main()
