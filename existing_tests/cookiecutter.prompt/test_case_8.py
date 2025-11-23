import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            dict_0 = None
            float_0 = 32.888
            list_0 = [dict_0, dict_0, dict_0, float_0]
            float_1 = 255.19
            int_0 = -275
            str_0 = ''
            float_2 = 2283.45192
            var_0 = module_0.prompt_choice_for_config(list_0, float_1, int_0, str_0, float_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
