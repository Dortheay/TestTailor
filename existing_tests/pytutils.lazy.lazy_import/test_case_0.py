import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x8f\xc1\xf9\xc5\xdf\xb9\xea\x08\x0b\x07\xcc[\xbd)\xcc\xc3j1\xb6'
            bool_0 = False
            illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(bytes_0, bool_0)
            var_0 = illegal_use_of_scope_replacer_0.__unicode__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
