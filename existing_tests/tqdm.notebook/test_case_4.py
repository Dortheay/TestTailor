import unittest
import timeout_decorator
import tqdm.notebook as module_0

class Test_Notebook_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        tqdm_h_box_0 = module_0.TqdmHBox()
        var_0 = tqdm_h_box_0.__repr__()

if __name__ == "__main__":
    unittest.main()
