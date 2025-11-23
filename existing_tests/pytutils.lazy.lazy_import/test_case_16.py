import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        import_processor_0 = module_0.ImportProcessor()
        bool_0 = True
        list_0 = [bool_0, bool_0]
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(bool_0, list_0)
        var_0 = illegal_use_of_scope_replacer_0.__eq__(import_processor_0)

if __name__ == "__main__":
    unittest.main()
