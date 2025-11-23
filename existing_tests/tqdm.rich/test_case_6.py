import unittest
import timeout_decorator
import tqdm.rich as module_0
import rich.progress as module_1

class Test_Rich_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = -12
            str_0 = "H3=mzmt,f@y'z5"
            float_0 = 1000.0
            float_1 = 0.0
            float_2 = 5120.0
            var_0 = {}
            task_0 = module_1.Task(int_0, str_0, float_0, float_1, var_0)
            str_1 = 'B'
            bool_0 = False
            int_1 = 1024
            rate_column_0 = module_0.RateColumn(str_1, bool_0, int_1)
            var_1 = rate_column_0.render(task_0)
            bool_1 = True
            rate_column_1 = module_0.RateColumn(str_1, bool_1, int_1)
            var_2 = rate_column_1.render(task_0)
            tqdm_rich_0 = module_0.tqdm_rich()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
