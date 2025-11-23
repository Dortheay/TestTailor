import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'test_replay_dir'
            str_1 = 'test_template'
            str_2 = 'name'
            str_3 = 'test_project'
            str_4 = {str_2: str_3}
            str_5 = {str_0: str_4}
            var_0 = str_1 + str_1
            var_1 = module_0.dump(str_0, str_1, str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
