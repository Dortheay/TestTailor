import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            dict_0 = {}
            int_0 = -115
            list_0 = [int_0, int_0]
            var_0 = module_0.prompt_choice_for_config(list_0, list_0, list_0, dict_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
