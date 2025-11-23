import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        str_0 = 'j|#QXia\\a\\rVNNt'
        file_skip_setting_0 = module_0.FileSkipSetting(str_0)
        str_1 = '@'
        file_skipped_0 = module_0.FileSkipped(str_0, str_1)
        file_skip_setting_1 = module_0.FileSkipSetting(str_0)
        str_2 = '/__init__.py'
        introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_2)
        str_3 = "4_qifpb-jiP'4/"
        list_0 = [file_skip_setting_0]
        type_0 = module_1.type(*list_0)
        literal_sort_type_mismatch_0 = module_0.LiteralSortTypeMismatch(type_0, type_0)
        missing_section_0 = module_0.MissingSection(str_0, str_3)

if __name__ == "__main__":
    unittest.main()
