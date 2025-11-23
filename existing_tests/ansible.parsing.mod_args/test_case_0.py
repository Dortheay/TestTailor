import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '[->2Km0\r>[[`rVOu'
            module_args_parser_0 = module_0.ModuleArgsParser(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
