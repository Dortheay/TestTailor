import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            dict_0 = {}
            str_0 = '6Z{'
            set_0 = None
            str_1 = ''
            dict_1 = {set_0: set_0, str_1: str_0}
            str_2 = None
            var_0 = module_0.render_variable(dict_0, dict_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
