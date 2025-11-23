import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'AB\rnw\n:'
        introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_0)
        str_1 = '3 _Sp'
        invalid_settings_path_0 = module_0.InvalidSettingsPath(str_1)
        str_2 = '>n6?j^-vr'
        existing_syntax_errors_0 = module_0.ExistingSyntaxErrors(str_2)

if __name__ == "__main__":
    unittest.main()
