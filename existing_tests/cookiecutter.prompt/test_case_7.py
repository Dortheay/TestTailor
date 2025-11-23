import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = -81
            bool_0 = True
            str_0 = '6Z{'
            var_0 = module_0.render_variable(bool_0, int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
