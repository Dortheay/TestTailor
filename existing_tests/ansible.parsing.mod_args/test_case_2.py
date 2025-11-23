import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            module_args_parser_0 = module_0.ModuleArgsParser()
            dict_0 = {module_args_parser_0: module_args_parser_0, module_args_parser_0: module_args_parser_0}
            module_args_parser_1 = module_0.ModuleArgsParser(dict_0)
            var_0 = module_args_parser_1.parse()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
