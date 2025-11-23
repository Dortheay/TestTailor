import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'Hb#h|9^'
            var_0 = module_0.prompt_for_config(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
