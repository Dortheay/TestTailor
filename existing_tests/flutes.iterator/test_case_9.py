import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            iterator_0 = None
            str_0 = 'mW!h!cDl'
            var_0 = module_0.scanr(iterator_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
