import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = ",J&,9\n5*'"
            float_0 = -2208.0
            dict_0 = {str_0: str_0, float_0: str_0}
            int_0 = -1225
            numeric_0 = module_0._Numeric(int_0)
            var_0 = numeric_0.__lt__(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
