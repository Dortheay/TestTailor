import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            map_list_0 = None
            bytes_0 = b'K\x0ew25T\xba'
            str_0 = ')Xm4/\x0bz@|5nWa4r'
            map_list_1 = module_0.MapList(bytes_0, str_0)
            var_0 = map_list_1.__getitem__(map_list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
