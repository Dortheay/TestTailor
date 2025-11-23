import unittest
import timeout_decorator
import tqdm.notebook as module_0

class Test_Notebook_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = None
            set_0 = {float_0, float_0}
            list_0 = [set_0, float_0, float_0]
            tqdm_notebook_0 = module_0.tqdm_notebook(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
