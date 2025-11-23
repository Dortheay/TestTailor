import unittest
import timeout_decorator
import tqdm.contrib.itertools as module_0

class Test_Itertools_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'a'
        str_1 = 'b'
        str_2 = [str_0, str_1]
        var_0 = module_0.product(*str_2)
        var_1 = list(var_0)
        var_2 = len(var_1)

if __name__ == "__main__":
    unittest.main()
