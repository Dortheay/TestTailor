import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            int_0 = -81
            str_0 = '6Z{'
            list_0 = [int_0, int_0]
            var_0 = module_0.read_user_choice(str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
