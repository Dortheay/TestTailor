import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'gh:example_project'
        str_1 = 'gh'
        str_2 = 'https://github.com/{}.git'
        str_3 = {str_1: str_2}
        var_0 = module_0.expand_abbreviations(str_0, str_3)
        str_4 = 'example'
        str_5 = 'example'
        str_6 = 'https://github.com/example_project.git'
        str_7 = {str_5: str_6}
        var_1 = module_0.expand_abbreviations(str_4, str_7)
        str_8 = 'unknown:project'
        str_9 = {str_1: str_2}
        var_2 = module_0.expand_abbreviations(str_8, str_9)

if __name__ == "__main__":
    unittest.main()
