import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            int_0 = 0
            iterator_0 = module_0.split_by(int_0, criterion=int_0)
            var_0 = list(iterator_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
