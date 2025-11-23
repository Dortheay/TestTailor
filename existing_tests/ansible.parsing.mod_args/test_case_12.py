import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'action'
        str_1 = 'module'
        str_2 = 'i'
        str_3 = "shell echo 'Hello World'"
        str_4 = {str_0: str_3, str_2: str_1, str_1: str_1}
        var_0 = {}
        module_args_parser_0 = module_0.ModuleArgsParser(str_4)
        module_args_parser_1 = module_0.ModuleArgsParser(var_0)
        var_1 = module_args_parser_0.parse()
        module_args_parser_2 = module_0.ModuleArgsParser()

if __name__ == "__main__":
    unittest.main()
