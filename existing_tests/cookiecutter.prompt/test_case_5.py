import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'IPV)lH(Uari|'
            float_0 = -955.0725
            tuple_0 = None
            str_1 = "$/'^!@H2"
            dict_0 = {float_0: tuple_0, float_0: float_0, str_1: str_0, tuple_0: tuple_0}
            var_0 = module_0.read_user_dict(tuple_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
