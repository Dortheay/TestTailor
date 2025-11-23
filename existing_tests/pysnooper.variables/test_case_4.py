import unittest
import timeout_decorator
import pysnooper.variables as module_0

class Test_Variables_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '~exception'
            indices_0 = module_0.Indices(str_0)
            var_0 = indices_0.__getitem__(indices_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
