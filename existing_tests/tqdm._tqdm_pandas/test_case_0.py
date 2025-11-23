import unittest
import timeout_decorator
import tqdm._tqdm_pandas as module_0

class Test__tqdm_pandas_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -3083
            var_0 = module_0.tqdm_pandas(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
