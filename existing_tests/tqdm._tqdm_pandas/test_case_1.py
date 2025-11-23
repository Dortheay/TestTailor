import unittest
import timeout_decorator
import tqdm._tqdm_pandas

class Test__tqdm_pandas_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
