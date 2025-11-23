import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            var_0 = module_0.read_user_variable(list_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
