import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            scope_replacer_0 = None
            illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(scope_replacer_0, scope_replacer_0)
            str_0 = 'f;&Lz@&8=43\\NBL7l;,?'
            var_0 = module_0.lazy_import(illegal_use_of_scope_replacer_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
