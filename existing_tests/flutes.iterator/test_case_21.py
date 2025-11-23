import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = -3860
            list_0 = [int_0]
            range_0 = module_0.Range(*list_0)
            var_0 = range_0.__getitem__(int_0)
            range_1 = module_0.Range()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
