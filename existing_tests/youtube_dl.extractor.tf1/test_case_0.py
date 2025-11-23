import unittest
import timeout_decorator
import youtube_dl.extractor.tf1 as module_0

class Test_Tf1_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        t_f1_i_e_0 = module_0.TF1IE()

if __name__ == "__main__":
    unittest.main()
