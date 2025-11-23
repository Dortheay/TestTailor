import unittest
import timeout_decorator
import tqdm.notebook as module_0

class Test_Notebook_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            list_1 = [list_0, list_0, list_0]
            var_0 = module_0.tnrange(*list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
