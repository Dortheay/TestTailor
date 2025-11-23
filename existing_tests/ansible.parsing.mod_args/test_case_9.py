import unittest
import timeout_decorator
import ansible.parsing.mod_args as module_0

class Test_Mod_args_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        module_args_parser_0 = module_0.ModuleArgsParser()

if __name__ == "__main__":
    unittest.main()
