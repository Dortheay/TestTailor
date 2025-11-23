import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'i'
            var_0 = module_0.read_user_choice(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
