import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'Q\r;3\\1q'
            str_1 = 'L>E&JYF;{I3q'
            var_0 = module_0.load(str_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
