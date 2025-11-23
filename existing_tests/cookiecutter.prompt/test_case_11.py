import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            dict_0 = {}
            int_0 = -81
            list_0 = [int_0, int_0]
            float_0 = 494.8877941008026
            var_0 = module_0.render_variable(dict_0, list_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
