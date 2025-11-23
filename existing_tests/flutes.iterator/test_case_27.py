import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            int_0 = -1634
            bytes_0 = b'\x19`G\x80\xf8tlG\xb1\xa0\x0c\xaa\x13\xbe'
            lazy_list_0 = module_0.LazyList(bytes_0)
            var_0 = lazy_list_0.__getitem__(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
