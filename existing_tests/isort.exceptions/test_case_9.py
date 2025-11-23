import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = '\x0bbhYlOI_Ci'
        str_1 = ''
        invalid_settings_path_0 = module_0.InvalidSettingsPath(str_1)
        missing_section_0 = module_0.MissingSection(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
