import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'et'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            set_0 = None
            module_args_parser_0 = module_0.ModuleArgsParser(dict_0, set_0)
            module_args_parser_1 = module_0.ModuleArgsParser()
            str_1 = "shell echo 'Hello World'"
            var_0 = module_args_parser_0.parse(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
