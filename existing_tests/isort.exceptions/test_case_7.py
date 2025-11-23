import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '--length-sort'
        profile_does_not_exist_0 = module_0.ProfileDoesNotExist(str_0)
        str_1 = '%wH+\\&g86}'
        str_2 = '5B vvF,2\x0cl2\x0cV/xA'
        file_skip_setting_0 = module_0.FileSkipSetting(str_2)
        str_3 = 'heapq'
        str_4 = "%/cc_N'\x0b\n{"
        assignments_format_mismatch_0 = module_0.AssignmentsFormatMismatch(str_4)
        file_skip_setting_1 = module_0.FileSkipSetting(str_3)
        existing_syntax_errors_0 = module_0.ExistingSyntaxErrors(str_1)

if __name__ == "__main__":
    unittest.main()
