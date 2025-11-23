import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'cookiecutter'
        str_1 = {str_0: str_0}
        var_0 = module_0.dump(str_0, str_0, str_1)

if __name__ == "__main__":
    unittest.main()
