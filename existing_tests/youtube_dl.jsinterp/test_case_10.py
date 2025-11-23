import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = False
        bool_1 = False
        j_s_interpreter_0 = module_0.JSInterpreter(bool_0, bool_1)

if __name__ == "__main__":
    unittest.main()
