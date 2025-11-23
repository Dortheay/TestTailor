import unittest
import timeout_decorator
import tqdm.contrib.itertools as module_0

class Test_Itertools_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -1945
            str_0 = ''
            var_0 = (int_0, str_0)
            var_1 = module_0.product(*var_0)
            var_2 = list(var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
