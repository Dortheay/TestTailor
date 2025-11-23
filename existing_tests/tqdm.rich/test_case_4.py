import unittest
import timeout_decorator
import tqdm.rich as module_0
import rich.progress as module_1

class Test_Rich_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            var_0 = module_0.trrange()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
