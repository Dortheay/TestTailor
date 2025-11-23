import unittest
import timeout_decorator
import tqdm.rich as module_0
import rich.progress as module_1

class Test_Rich_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = None
            fraction_column_0 = module_0.FractionColumn()
            var_0 = fraction_column_0.render(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
