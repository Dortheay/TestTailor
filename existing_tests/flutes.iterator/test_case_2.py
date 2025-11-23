import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = 0.1
        float_1 = 1584.19828
        str_0 = 'O'
        map_list_0 = module_0.MapList(float_1, str_0)
        list_0 = [float_0]
        range_0 = module_0.Range(*list_0)
        int_0 = 2861
        iterable_0 = None
        iterator_0 = module_0.take(int_0, iterable_0)
        iterator_1 = range_0.__iter__()

if __name__ == "__main__":
    unittest.main()
