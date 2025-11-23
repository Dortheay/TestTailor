import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '}_m\x0bc1|}sn|v'
            int_0 = -1287
            list_0 = [str_0, int_0, str_0, str_0]
            str_1 = '.json'
            var_0 = module_0.load(list_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
