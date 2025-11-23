import unittest
import timeout_decorator
import tqdm.rich as module_0
import rich.progress as module_1

class Test_Rich_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            rate_column_0 = module_0.RateColumn()
            var_0 = rate_column_0.render(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
