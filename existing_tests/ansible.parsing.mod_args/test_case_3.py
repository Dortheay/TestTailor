import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'module'
            str_1 = 'dest'
            str_2 = 'local_action'
            str_3 = "shell echo 'Hello World'"
            str_4 = {str_2: str_3, str_1: str_0, str_1: str_1}
            module_args_parser_0 = module_0.ModuleArgsParser(str_4)
            var_0 = module_args_parser_0.parse(module_args_parser_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
