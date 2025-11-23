import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'j|#QXia\\a\\rVNNt'
        file_skip_setting_0 = module_0.FileSkipSetting(str_0)
        str_1 = '@'
        file_skipped_0 = module_0.FileSkipped(str_0, str_1)
        file_skip_setting_1 = module_0.FileSkipSetting(str_0)
        str_2 = '/__init__.py'
        introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_2)
        str_3 = "4_qifpb-jiP'4/"
        missing_section_0 = module_0.MissingSection(str_0, str_3)

if __name__ == "__main__":
    unittest.main()
