import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '-v'
            tuple_0 = ()
            list_0 = [str_0, str_0, tuple_0, tuple_0]
            float_0 = 789.8857
            float_1 = 1159.0
            var_0 = module_0.render_variable(float_0, list_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
