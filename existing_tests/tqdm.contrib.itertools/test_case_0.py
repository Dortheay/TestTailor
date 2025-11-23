import unittest
import timeout_decorator
import tqdm.contrib.itertools as module_0

class Test_Itertools_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.product()

if __name__ == "__main__":
    unittest.main()
