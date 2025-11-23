import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'AL#\r6^'
            bytes_0 = b'W\x8f\x9a2\x88\xf3\xf9\x02\x08\x15\x94\xb2'
            var_0 = module_0.dump(str_0, str_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
