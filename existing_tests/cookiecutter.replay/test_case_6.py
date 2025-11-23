import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = 1984.7938
            dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
            var_0 = module_0.load(float_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
