import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'dest'
        module_args_parser_0 = module_0.ModuleArgsParser()
        str_1 = 'copy'
        str_2 = 'i'
        str_3 = {str_2: str_1, str_2: str_2, str_0: str_1}
        str_4 = 'local_action'
        str_5 = "shell echo 'Hello World'"
        str_6 = {str_4: str_5, str_2: str_2, str_0: str_0}
        module_args_parser_1 = module_0.ModuleArgsParser(str_6)
        module_args_parser_2 = module_0.ModuleArgsParser(str_3)
        var_0 = module_args_parser_1.parse()

if __name__ == "__main__":
    unittest.main()
