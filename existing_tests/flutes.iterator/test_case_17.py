import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 2173
            float_0 = 3176.8076
            list_0 = [int_0]
            list_1 = [float_0, float_0]
            range_0 = module_0.Range(*list_1)
            var_0 = range_0.__getitem__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
