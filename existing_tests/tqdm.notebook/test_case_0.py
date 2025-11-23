import unittest
import timeout_decorator
import tqdm.notebook as module_0

class Test_Notebook_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tqdm_notebook_0 = module_0.tqdm_notebook()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
