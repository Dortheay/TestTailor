import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = None
            list_0 = [int_0, int_0, int_0]
            str_0 = 'E:* hU\nsyF1*-Q'
            var_0 = module_0.render_variable(int_0, list_0, str_0)
            dict_0 = {}
            bool_0 = False
            var_1 = module_0.read_user_dict(dict_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
