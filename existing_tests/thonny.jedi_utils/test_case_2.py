import unittest
import timeout_decorator
import thonny.jedi_utils as module_0

class Test_Jedi_utils_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '`*SHdDpt\tFZH'
            int_0 = 2685
            int_1 = 716
            str_1 = '!Gs:3\rYconA.1A=G{'
            var_0 = module_0.get_script_completions(str_0, int_0, int_1, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
