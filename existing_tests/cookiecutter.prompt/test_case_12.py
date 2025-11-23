import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            bytes_0 = b'\xbbf\xc5\x92\x00\xcf{'
            tuple_0 = (bytes_0,)
            bool_0 = False
            bool_1 = False
            float_0 = 4767.28
            dict_0 = {float_0: tuple_0, bool_1: bool_1}
            var_0 = module_0.prompt_choice_for_config(tuple_0, bool_0, bool_1, bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
