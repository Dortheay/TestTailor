import unittest
import timeout_decorator
import pytutils.env as module_0

class Test_Env_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = "TEST='${HOME}/example'"
        str_1 = 'PATH="/usr/bin:/bin"'
        str_2 = "EMPTY=''"
        str_3 = 'QUOTED="escaped\\"quotes"'
        str_4 = 'INVALID_LINE_NOT_PARSED'
        str_5 = [str_0, str_1, str_2, str_3, str_4]
        generator_0 = module_0.parse_env_file_contents(str_5)
        var_0 = list(generator_0)

if __name__ == "__main__":
    unittest.main()
