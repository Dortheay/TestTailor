import unittest
import timeout_decorator
import pytutils.env as module_0

class Test_Env_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'TEST=${HOME}/yeee'
        str_1 = 'THISIS=~/a/test'
        str_2 = "YOLO='~/swaggins/$NONEXISTENT_VAR'"
        str_3 = [str_0, str_1, str_2]
        generator_0 = module_0.parse_env_file_contents(str_3)
        var_0 = list(generator_0)

if __name__ == "__main__":
    unittest.main()
