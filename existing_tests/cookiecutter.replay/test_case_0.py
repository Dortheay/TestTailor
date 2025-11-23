import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'lj$7ORT-(!Fl;MW4h)x'
        var_0 = module_0.get_file_name(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
