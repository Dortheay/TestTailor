import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '--replay'
            int_0 = 1789
            var_0 = module_0.read_user_dict(str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
