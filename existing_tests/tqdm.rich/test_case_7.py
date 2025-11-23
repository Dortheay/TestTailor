import unittest
import timeout_decorator
import tqdm.rich as module_0
import rich.progress as module_1

class Test_Rich_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        fraction_column_0 = module_0.FractionColumn()

if __name__ == "__main__":
    unittest.main()
