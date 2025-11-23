import unittest
import timeout_decorator
import thefuck.rules.scm_correction as module_0

class Test_Scm_correction_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = None
            var_0 = module_0.get_new_command(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
