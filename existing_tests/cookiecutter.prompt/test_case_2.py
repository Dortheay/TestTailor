import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            int_0 = -81
            list_0 = [int_0, int_0]
            float_0 = 494.5469
            var_0 = module_0.render_variable(list_0, dict_0, float_0)
            str_0 = 'S'
            var_1 = module_0.read_user_yes_no(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
