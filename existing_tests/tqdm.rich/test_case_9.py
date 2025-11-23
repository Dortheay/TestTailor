import unittest
import timeout_decorator
import tqdm.rich as module_0
import rich.progress as module_1

class Test_Rich_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 1
        str_0 = '+o%y#Rus)0h_g<y\r^8\x0c0'
        float_0 = 0.0
        float_1 = 5120.0
        var_0 = {}
        task_0 = module_1.Task(int_0, str_0, float_0, float_0, var_0)
        str_1 = 'B'
        int_1 = 1024
        bool_0 = True
        rate_column_0 = module_0.RateColumn(str_1, bool_0, int_1)
        var_1 = rate_column_0.render(task_0)
        bool_1 = False
        rate_column_1 = module_0.RateColumn(str_1, bool_1, int_1)

if __name__ == "__main__":
    unittest.main()
