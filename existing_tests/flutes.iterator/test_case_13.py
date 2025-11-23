import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -157
            set_0 = {int_0, int_0, int_0}
            iterable_0 = None
            iterator_0 = module_0.chunk(int_0, iterable_0)
            list_0 = [set_0, int_0, int_0]
            range_0 = module_0.Range(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
