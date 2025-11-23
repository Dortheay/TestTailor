import unittest
import timeout_decorator
import thonny.jedi_utils as module_0

class Test_Jedi_utils_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -4773
            str_0 = ';[\rh9F/+cha#7\n'
            bytes_0 = b'\xa5rJuu'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: bytes_0}
            float_0 = 3507.3
            thonny_completion_0 = module_0.ThonnyCompletion(str_0, str_0, str_0, dict_0, dict_0, float_0)
            var_0 = thonny_completion_0.__getitem__(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
