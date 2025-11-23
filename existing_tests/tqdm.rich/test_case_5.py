import unittest
import timeout_decorator
import tqdm.rich as module_0
import rich.progress as module_1

class Test_Rich_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'B'
            int_0 = 1024
            bool_0 = True
            rate_column_0 = module_0.RateColumn(str_0, bool_0, int_0)
            tqdm_rich_0 = module_0.tqdm_rich()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
