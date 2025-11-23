import unittest
import timeout_decorator
import tqdm.notebook as module_0

class Test_Notebook_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            tqdm_h_box_0 = module_0.TqdmHBox()
            var_0 = tqdm_h_box_0.__repr__(tqdm_h_box_0)
            var_1 = tqdm_h_box_0.__repr__()
            tqdm_notebook_0 = module_0.tqdm_notebook()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
