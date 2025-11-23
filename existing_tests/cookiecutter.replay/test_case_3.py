import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'UHable tA d,code toJSON.'
            set_0 = {str_0, str_0, str_0}
            tuple_0 = (str_0, str_0, set_0)
            var_0 = module_0.dump(str_0, tuple_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
