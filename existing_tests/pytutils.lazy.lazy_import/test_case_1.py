import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'test_name'
            illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(str_0, str_0, str_0)
            var_0 = illegal_use_of_scope_replacer_0.__unicode__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
