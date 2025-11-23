import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '.'
        iterator_0 = module_0.split_by(str_0, separator=str_0)
        var_0 = list(iterator_0)
        bytes_0 = b'l\xfc\xf6\xe9\xff\x05\xe4\xcf\x18\x9a\xb2\x82\x13\xe3\xdem'
        lazy_list_0 = module_0.LazyList(bytes_0)
        int_0 = None
        callable_0 = None
        iterable_0 = None
        iterator_1 = module_0.drop_until(callable_0, iterable_0)
        bool_0 = True
        iterator_2 = module_0.chunk(int_0, bool_0)
        iterator_3 = module_0.split_by(bool_0)
        var_1 = lazy_list_0.__getitem__(bool_0)
        iterable_1 = None
        iterator_4 = module_0.split_by(iterable_1)

if __name__ == "__main__":
    unittest.main()
