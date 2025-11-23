import unittest
import timeout_decorator
import thonny.jedi_utils as module_0

class Test_Jedi_utils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = None
            list_0 = []
            var_0 = module_0.get_interpreter_completions(str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
