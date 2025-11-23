import unittest
import timeout_decorator
import cookiecutter.replay as module_0

class Test_Replay_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b''
            str_0 = '~-Q==#u'
            set_0 = set()
            var_0 = module_0.dump(bytes_0, str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
