import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = -61.0
            complex_0 = None
            var_0 = module_0.dump(float_0, float_0, complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
