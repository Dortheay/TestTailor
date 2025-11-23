import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            dict_0 = {}
            bytes_0 = b'5'
            tuple_0 = ()
            var_0 = module_0.lazy_import(dict_0, bytes_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
